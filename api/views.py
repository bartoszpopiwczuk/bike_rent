from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


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