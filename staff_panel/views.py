from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Q
from django.shortcuts import redirect, render
from django.utils import timezone

from bike_portfolio.models import Bicycle
from bike_portfolio.utils import paginateBicycles

from .forms import AddBikeForm, AddIssueForm
from .models import Issue


@staff_member_required
def staff_main(request):
    objects = Bicycle.objects.annotate(
        # adds extra field to each bike not stored in the database
        unresolved_issues_count=Count(
            # counts the number of related issues with is_fixed=False
            "repair_logs",
            filter=Q(repair_logs__is_fixed=False),
            # stores the count in the extra field
        )
    ).order_by("-unresolved_issues_count")  # "-" means descending order

    # Pagination
    bikes, paginator = paginateBicycles(request, objects, objects_per_page=5)

    context = {
        "website_title": "bikes.com - Staff Panel - Main",
        "bike_list": bikes,
        "paginator": paginator,
    }
    return render(request, "staff_panel/home.html", context)


@staff_member_required
def staff_detail(request, pk):
    bike: Bicycle = Bicycle.objects.get(id=pk)
    context = {
        "website_title": f"bikes.com - Staff Panel - {bike.brand} {bike.line} {bike.model}",
        "bike": bike,
        "issues": bike.repair_logs.filter(is_fixed=False),  # type: ignore
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
        if form.is_valid():
            issue = form.save(commit=False)
            issue.bicycle = bike
            issue.reported_by = request.user
            issue.save()
            messages.success(request, "Issue added successfully")
        return redirect("staff-main")
    else:
        form = AddIssueForm()

    context = {
        "website_title": f"bikes.com - Staff Panel - Add Issue to {bike.brand} {bike.line} {bike.model}",
        "form": form,
        "bike": bike,
    }

    return render(request, "staff_panel/add_issue.html", context)


@staff_member_required
def staff_delete_issue(request, pk):
    if request.method == "POST":
        issue = Issue.objects.get(id=pk)
        issue.is_fixed = True
        issue.date_fixed = timezone.now()
        issue.fixed_by = request.user
        issue.save()
        messages.success(request, "Issue marked as fixed")
    return redirect("staff-main")  # if not POST


@staff_member_required
def staff_edit_issue(request, pk):
    issue = Issue.objects.get(id=pk)
    if request.method == "POST":  # POST request: you submit the form
        form = AddIssueForm(request.POST, request.FILES or None, instance=issue)
        if form.is_valid():
            form.save()
            messages.success(request, "Issue updated successfully")
            print("all good")
            next_url = request.POST.get(
                "current-page", "staff-main"
            )  # Optional: Redirect back to current page
            return redirect(next_url)
    else:  # GET request: you get this to see the form
        form = AddIssueForm(instance=issue)

    context = {
        "website_title": f"bikes.com - Staff Panel - Edit Issue #{issue.id}",
        "form": form,
        "issue": issue,
        "bike": issue.bicycle,
    }

    return render(request, "staff_panel/edit_issue.html", context)


def staff_add_bike(request):
    if request.method == "POST":
        form = AddBikeForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Bike added successfully")
            return redirect("staff-main")
    else:
        form = AddBikeForm()

    context = {
        "website_title": "bikes.com - Staff Panel - Add Bike",
        "form": form,
    }

    return render(request, "staff_panel/add_bike.html", context)


@staff_member_required
def staff_delete_bike(request, pk):
    if request.method == "POST":
        bike = Bicycle.objects.get(id=pk)
        if bike.repair_logs.exists():  # type: ignore
            bike.repair_logs.all().delete()  # type: ignore
        bike.delete()
        messages.success(request, "Bike has been deleted successfully")
    return redirect("staff-main")


@staff_member_required
def staff_edit_bike(request, pk):
    bike = Bicycle.objects.get(id=pk)
    if request.method == "POST":
        form = AddBikeForm(request.POST, request.FILES or None, instance=bike)
        if form.is_valid():
            form.save()
            messages.success(request, "Bike updated successfully")
            return redirect("staff-main")
    else:
        form = AddBikeForm(instance=bike)

    context = {
        "website_title": f"bikes.com - Staff Panel - Edit Bike #{bike.id}",
        "form": form,
        "bike": bike,
    }

    return render(request, "staff_panel/edit_bike.html", context)


@staff_member_required
def staff_mark_available(request, pk):
    bike = Bicycle.objects.get(id=pk)
    if bike.is_available:
        bike.is_available = False
        messages.success(request, "Bike marked as unavailable")
        bike.save()
    elif bike.is_available == False:
        bike.is_available = True
        messages.success(request, "Bike marked as available")
        bike.save()
    return redirect("staff-main")
