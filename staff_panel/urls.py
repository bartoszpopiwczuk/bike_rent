from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_main, name="staff-main"),
]
