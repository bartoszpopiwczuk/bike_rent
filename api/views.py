from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bike_portfolio.models import Bicycle

from .serializers import BicycleSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/bikes'},
        {'GET': '/api/bikes/id'},
        {'POST': '/api/bikes/id/review'},

        {'POST': '/api/bikes/token'},
        {'POST': '/api/bikes/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
def getBicycles(request):
    bikes = Bicycle.objects.all()
    serializer = BicycleSerializer(bikes, many=True)
    return Response(serializer.data)
