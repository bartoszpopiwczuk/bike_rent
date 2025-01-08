from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from bike_portfolio.models import Bicycle
from django.db.models import Count, Q
from .forms import AddIssueForm
from django.shortcuts import redirect


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
        "issues": bike.repair_logs.all(),
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


@staff_member_required
def staff_add_issue(request, pk):
    bike = Bicycle.objects.get(id=pk)
    if request.method == "POST":
        form = AddIssueForm(request.POST, request.FILES or None)
        issue = form.save(commit=False)
        issue.bicycle = bike
        issue.reported_by = request.user
        issue.save()
        return redirect("staff-main")
    else:
        form = AddIssueForm()

    context = {
        "website_title": f"bikes.com - Staff Panel - Add Issue to {bike.brand} {bike.line} {bike.model}",
        "form": form,
        "bike": bike,
    }

    return render(request, "staff_panel/add_issue.html", context)
