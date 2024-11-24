from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]
