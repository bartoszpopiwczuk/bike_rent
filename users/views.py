from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from bike_portfolio.models import Bicycle

from .forms import UserLoginForm, UserRegisterForm
from .models import Favorite


def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account created")
            login(request, form.instance)
            return redirect("all-bikes")
    else:
        form = UserRegisterForm()
    context = {"form": form}
    return render(request, "users/register.html", context)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        email = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(
                request, f"Logged in as {user.first_name} {user.last_name}"
            )
            return redirect("all-bikes")
        else:
            messages.error(request, "Email or password is incorrect")
    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "users/login.html", context)


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, f"You have been succesfully logged out.")
    return redirect("all-bikes")


@login_required
def add_favorite(request, pk):
    if request.method == "POST":
        bike = Bicycle.objects.get(id=pk)
        favorite, created = Favorite.objects.get_or_create(user=request.user, bike=bike)
        if created:
            messages.success(request, f"{bike} has been added to your favourites")
        else:
            favorite.delete()
            messages.info(request, f"{bike} is deleted from your favorites")
    return redirect(request.POST.get("next", "bike-detail"))


@login_required
def my_favorites(request):
    favorite_bikes = Bicycle.objects.filter(favorite__user=request.user).order_by(
        "-is_available"
    )
    context = {"bike_list": favorite_bikes}
    return render(request, "users/my_favorites.html", context)
