from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from bike_portfolio.models import Bicycle


@staff_member_required
def staff_main(request):
    bike_list_sorted = sorted(
        Bicycle.objects.all(), key=lambda bike: bike.repair is not None, reverse=True
    )
    context = {
        "website_title": "Staff Panel",
        "bike_list": bike_list_sorted,
    }
    return render(request, "staff_panel/home.html", context)
