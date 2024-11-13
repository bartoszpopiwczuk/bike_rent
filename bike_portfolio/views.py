from django.shortcuts import render
from django.http import HttpResponse

bike_list = [
    {
        "brand": "Trek",
        "model": "Slash 8",
        "year": "2018",
        "frame_size": "M",
        "tire_size": '29"',
    },
    {
        "brand": "Kellys",
        "model": "Swag 10",
        "year": "2019",
        "frame_size": "M",
        "tire_size": '27.5"',
    },
]


def all_bikes(request):
    context = {"website_title": "Choose your Bike", "bike_list": bike_list}
    return render(request, "bike_portfolio/home.html", context)
