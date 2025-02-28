from django.db.models import Q

from .models import Bicycle


def searchBicycles(request):
    search_query: str = ""
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
    )

    return objects, search_query
