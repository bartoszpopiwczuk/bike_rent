from django.shortcuts import render
from .models import Bicycle


def all_bikes(request):
    context = {"website_title": "Choose your Bike", "bike_list": Bicycle.objects.all()}
    return render(request, "bike_portfolio/home.html", context)
