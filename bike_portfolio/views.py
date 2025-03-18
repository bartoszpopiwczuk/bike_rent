from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Page, Paginator
from django.shortcuts import redirect, render
from django.urls import reverse

from users.models import Favorite

from .models import Bicycle
from .utils import paginateBicycles, searchBicycles


def all_bikes(request):

    # FIXME Search has to be working for other pages. Currently it is only working for home page. If I search in 'favorites' it should only show the bikes that are in favorites.

    # Search
    objects, search_query = searchBicycles(request, subset="all")

    # Pagination
    bikes, paginator = paginateBicycles(request, objects, objects_per_page=6)

    context = {
        "website_title": "bikes.com - Main",
        "bike_list": bikes,
        "search_query": search_query,
        "paginator": paginator,
        "go_after_search": "all-bikes",
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
    web_title = "bikes.com - Main" # default title to negate the risk of not finding the match
    for p in Bicycle.BICYCLE_PURPOSE_CHOICES:
        if purpose.lower() == p[0]:
            web_title = f"{p[1]} Bikes"
            break
    context = {
        "bike_list": Bicycle.objects.filter(purpose=purpose),
        "website_title": f"bikes.com - {web_title}",
        "go_after_search": reverse("bike-purpose", kwargs={"purpose": purpose}),
    }
    return render(request, "bike_portfolio/home.html", context)


def send_email(request):
    if request.method == "POST":

        send_mail(
            subject="Welcome to bikes.com - Django Project",
            message="""This is a test message
            Link to github: https://github.com/bartoszpopiwczuk""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.POST.get("email_recipient")],
            fail_silently=False,
        )

    return redirect(request.POST.get("next", "all-bikes"))
