from django.core.paginator import Paginator
from django.shortcuts import render

from users.models import Favorite

from .models import Bicycle


def all_bikes(request):
    objects = Bicycle.objects.all().order_by(
        "-is_available"
    )  # sorting by availablity, first True
    p = Paginator(objects, 6)
    page = request.GET.get("page")
    bikes = p.get_page(page)
    context = {
        "website_title": "bikes.com - Main",
        "bike_list": bikes,
    }
    return render(request, "bike_portfolio/home.html", context)


def bike_detail(request, pk):
    bike = Bicycle.objects.get(id=pk)
    if request.user.is_authenticated:
        is_fav = Favorite.objects.filter(user=request.user, bike=bike).exists()
    else:
        is_fav = False
    context = {
        "website_title": f"bikes.com - {bike.brand} {bike.line} {bike.model}",
        "bike": bike,
        "is_fav": is_fav,
    }
    return render(request, "bike_portfolio/bike_detail.html", context)


def bike_purpose(request, purpose):
    """Iterates over list of tuples. If puropses match, then the second element of the tuple will be name of the websie. Once match is made, the iteration stops."""
    for p in Bicycle.BICYCLE_PURPOSE_CHOICES:
        if purpose.lower() == p[0]:
            web_title = f"{p[1]} Bikes"
            break
    context = {
        "bike_list": Bicycle.objects.filter(purpose=purpose).order_by("-is_available"),
        "website_title": f"bikes.com - {web_title}",
    }
    return render(request, "bike_portfolio/home.html", context)
