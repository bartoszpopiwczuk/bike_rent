from django.shortcuts import render
from .models import Bicycle


def all_bikes(request):
    context = {"website_title": "Choose your Bike", "bike_list": Bicycle.objects.all()}
    return render(request, "bike_portfolio/home.html", context)


def bike_detail(request, pk):
    context = {
        "website_title": "Bike name X",
        "bike": Bicycle.objects.get(id=pk),  # TODO: fliter by id
    }
    return render(request, "bike_portfolio/bike_detail.html", context)
