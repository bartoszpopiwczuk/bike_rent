from django.urls import path

from . import views

urlpatterns = [
    path("", views.getRoutes),
    path("bicycles", views.getBicycles),
    path("bicycle/<str:pk>/", views.getBicycle), # it's better to pass id as type:str, because id can often contain letterseg. UUID
]
