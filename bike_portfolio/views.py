from django.shortcuts import render
from .models import Bicycle


def all_bikes(request):
    context = {"website_title": "Choose your Bike", "bike_list": Bicycle.objects.all()}
    return render(request, "bike_portfolio/home.html", context)


def bike_detail(request, pk):
    context = {
        "website_title": "Bike name X",
        "bike": Bicycle.objects.get(id=pk),
    }
    return render(request, "bike_portfolio/bike_detail.html", context)


def bike_purpose(request, purpose):
    for p in Bicycle.BICYCLE_PURPOSE_CHOICES:
        if purpose.lower() == p[0]:
            web_title = f"{p[1]} Bikes"
            break
    context = {
        "bike_list": Bicycle.objects.filter(purpose=purpose),
        "website_title": web_title,
    }
    return render(request, "bike_portfolio/home.html", context)
