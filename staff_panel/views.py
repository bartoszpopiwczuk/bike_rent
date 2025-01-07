from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from bike_portfolio.models import Bicycle
from django.db.models import Count, Q

@staff_member_required
def staff_main(request):
    bike_list_sorted = Bicycle.objects.annotate(
        unresolved_issues_count=Count(
            "repair_logs", filter=Q(repair_logs__is_fixed=False)
        )
    ).order_by("-unresolved_issues_count")
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
