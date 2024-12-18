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


def bike_purpose(request, purpose):
    if purpose == "mtb":
        web_title = "Mountain Bikes"
    elif purpose == "road":
        web_title = "Road Bikes "
    elif purpose == "gravel":
        web_title = "Gravel Bikes"
    elif purpose == "city":
        web_title = "City Bikes"
    else:
        web_title = "Other Bikes"

    context = {
        "website_title": web_title,
        "bike_list": Bicycle.objects.filter(purpose=purpose),
    }
    return render(request, "bike_portfolio/home.html", context)
