from django.urls import path
from . import views

urlpatterns = [
    path("", views.staff_main, name="staff-main"),
    path("details/<int:pk>", views.staff_detail, name="staff-detail"),
    path("repair/<int:pk>", views.staff_repair, name="staff-repair"),
]
