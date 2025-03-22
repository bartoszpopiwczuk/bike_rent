from django.core.paginator import Page, Paginator
from django.db.models import Q

from .models import Bicycle


def paginateBicycles(request, objects, objects_per_page) -> tuple:
    paginator = Paginator(objects, per_page=objects_per_page)
    page_number = request.GET.get("page")
    bikes: Page = paginator.get_page(number=page_number)

    return bikes, paginator


def searchBicycles(request, subset) -> tuple:
    search_query: str = ""

    # initial search query is going to be empty, empty string gives all objects, from chosen subset
    if type(subset) is list:
        objects = Bicycle.objects.filter(purpose=subset[0])
        print("subset is list")
    elif subset == "user_favorites":
        objects = Bicycle.objects.filter(favorites__user=request.user)
    else:
        objects = Bicycle.objects.all()

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query").strip()
        search_terms = search_query.split()
        query = Q()

        for q in search_terms:
            query |= (
                Q(brand__icontains=q)
                | Q(line__icontains=q)
                | Q(model__icontains=q)
                | Q(year_production__iexact=q)
                | Q(frame_size__iexact=q)
                | Q(frame_material__iexact=q)
                | Q(wheel_size__iexact=q)
                | Q(purpose__iexact=q)
            )
        if type(subset) is list:
            objects = objects.filter(purpose=subset[0]).distinct()
        elif subset == "user_favorites":
            objects = objects.filter(query, favorites__user=request.user).distinct()
        else:
            objects = Bicycle.objects.filter(query).distinct()

    return objects, search_query
