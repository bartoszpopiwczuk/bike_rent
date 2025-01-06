from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from bike_portfolio.models import Bicycle


@staff_member_required
def staff_main(request):
    bike_list_sorted: list[Bicycle] = sorted(
        Bicycle.objects.all(), key=lambda bike: bike.repair is not None, reverse=True
    )
    context = {
        "website_title": "bikes.com - Staff Panel - Main",
        "bike_list": bike_list_sorted,
    }
    return render(request, "staff_panel/home.html", context)


@staff_member_required
def staff_detail(request, pk):
    bike: Bicycle = Bicycle.objects.get(id=pk)
    context = {
        "website_title": f"bikes.com - Staff Panel - {bike.brand} {bike.line} {bike.model}",
        "bike": bike,
    }
    return render(request, "staff_panel/bike_detail.html", context)


@staff_member_required
def staff_repair(request, pk):
    bike: Bicycle = Bicycle.objects.get(id=pk)
    context = {
        "website_title": f"bikes.com - Staff Panel - {bike.brand} {bike.line} {bike.model}",
        "bike": bike,
    }
    return render(request, "staff_panel/bike_repair.html", context)
