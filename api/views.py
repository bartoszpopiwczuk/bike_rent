from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from bike_portfolio.models import Bicycle

from .serializers import BicycleSerializer, IssueSerializer


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {"GET": "/api/bikes"},
        {"GET": "/api/bikes/id"},
        {"POST": "/api/bikes/id/review"},
        {"POST": "/api/bikes/token"},
        {"POST": "/api/bikes/token/refresh"},
    ]
    return Response(routes)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])  # only authenticated users can access this api view, so you need to be logged to get the token and access this view
def getBicycles(request):
    bikes = Bicycle.objects.all()
    serializer = BicycleSerializer(bikes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getBicycle(request, pk):
    bike = Bicycle.objects.get(id=pk)
    serializer = BicycleSerializer(bike, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsAdminUser])
def addIssue(request, pk):
    try:
        bike = Bicycle.objects.get(id=pk)
    except Bicycle.DoesNotExist:
        return Response({"error": "Bike does not exist"}, status=404)  # not found
    data = request.data.copy()  # copy the data that is sent, because it's immutable
    data["bicycle"] = (
        bike.id
    )  # adding bike id automatically, so we don't need to pass it in JSON
    serializer = IssueSerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # created

    return Response(serializer.errors, status=400)  # bad request
