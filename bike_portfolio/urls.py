from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_bikes, name="all-bikes"),
    path("bike-detail/<int:pk>", views.bike_detail, name="bike-detail"),
]
