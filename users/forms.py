from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

field_formatting = "w-full bg-gray-600 bg-opacity-20 focus:bg-transparent focus:ring-2 focus:ring-yellow-900 rounded border border-gray-600 focus:border-yellow-500 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mb-4"


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": field_formatting,
                "placeholder": "First Name",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": field_formatting,
                "placeholder": "Last Name",
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": field_formatting,
                "placeholder": "Email",
            }
        )
    )
    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": field_formatting,
                "placeholder": "Password",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": field_formatting,
                "placeholder": "Repeat Password",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": field_formatting,
                "placeholder": "Email",
            }
        ),
        label="Email",
        max_length=254,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": field_formatting,
                "placeholder": "Password",
            }
        ),
        label="Password",
        max_length=254,
    )
