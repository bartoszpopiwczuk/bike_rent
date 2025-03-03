from django.core.paginator import Page, Paginator
from django.db.models import Q

from .models import Bicycle


def paginateBicycles(request, objects, objects_per_page) -> tuple:

    paginator = Paginator(objects, per_page=objects_per_page)
    page_number = request.GET.get("page")
    bikes: Page = paginator.get_page(number=page_number)

    return bikes, paginator


# TODO Make this work universally with different views


def searchBicycles(request) -> tuple:
    search_query: str = ""
    # initial search query is going to be empty, empty string gives all objects

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    objects = Bicycle.objects.filter(
        Q(brand__icontains=search_query)
        | Q(line__icontains=search_query)
        | Q(model__icontains=search_query)
        | Q(year_production__iexact=search_query)
        | Q(frame_size__iexact=search_query)
        | Q(frame_material__iexact=search_query)
        | Q(wheel_size__iexact=search_query)
        | Q(purpose__iexact=search_query)
    ).distinct()

    return objects, search_query
