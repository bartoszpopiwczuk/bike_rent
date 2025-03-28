from django.urls import path

from . import views

urlpatterns = [
    path("", views.all_bikes, name="all-bikes"),
    path("bike-detail/<str:pk>", views.bike_detail, name="bike-detail"),
    path("purpose/<str:purpose>", views.bike_purpose, name="bike-purpose"),
    path("send-email", views.send_email, name="send-email"),
]
