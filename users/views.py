from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm  # UserLogoutForm
from django.contrib.auth import authenticate, login
from .models import CustomUser


def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account created")
            return redirect("all-bikes")
    else:
        form = UserRegisterForm()
    context = {"form": form}
    return render(request, "users/register.html", context)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            try:
                user = CustomUser.objects.get(email=email)
            except:
                messages.error(request, "User does not exist")

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Logged in as {email}")
                return redirect("all-bikes")
            else:
                messages.error(request, "Email or password is incorrect")
    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "users/login.html", context)
