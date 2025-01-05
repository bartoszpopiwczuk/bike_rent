from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
