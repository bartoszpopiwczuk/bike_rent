from django.http import JsonResponse


def getRoutes(request):
    routes = [
        {'GET': '/api/bikes'},
        {'GET': '/api/bikes/id'},
        {'POST': '/api/bikes/id/review'},

        {'POST': '/api/bikes/token'},
        {'POST': '/api/bikes/token/refresh'},
    ]
    return JsonResponse(routes, safe=False)