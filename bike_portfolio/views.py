from django.shortcuts import render

from users.models import Favorite

from .models import Bicycle


def all_bikes(request):
    context = {
        "website_title": "bikes.com - Main",
        "bike_list": Bicycle.objects.all().order_by(
            "-is_available"
        ),  # sorting by availablity, first True
    }
    return render(request, "bike_portfolio/home.html", context)


def bike_detail(request, pk):
    bike = Bicycle.objects.get(id=pk)
    is_fav = Favorite.objects.filter(user=request.user, bike=bike).exists()
    context = {
        "website_title": f"bikes.com - {bike.brand} {bike.line} {bike.model}",
        "bike": bike,
        "is_fav": is_fav,
    }
    return render(request, "bike_portfolio/bike_detail.html", context)


def bike_purpose(request, purpose):
    for p in Bicycle.BICYCLE_PURPOSE_CHOICES:
        if purpose.lower() == p[0]:
            web_title = f"{p[1]} Bikes"
            break
    context = {
        "bike_list": Bicycle.objects.filter(purpose=purpose).order_by("-is_available"),
        "website_title": f"bikes.com - {web_title}",
    }
    return render(request, "bike_portfolio/home.html", context)
