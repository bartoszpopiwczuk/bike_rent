from django.urls import path
from . import views

urlpatterns = [
    path("", views.staff_main, name="staff-main"),
    path("details/<int:pk>", views.staff_detail, name="staff-detail"),
    path("repair/<int:pk>", views.staff_repair, name="staff-repair"),
    path("add-issue/<int:pk>", views.staff_add_issue, name="staff-add-issue"),
    path("delete-issue/<int:pk>", views.staff_delete_issue, name="staff-delete-issue"),
    path("edit-issue/<int:pk>", views.staff_edit_issue, name="staff-edit-issue"),
    path("add-bike/", views.staff_add_bike, name="staff-add-bike"),
    path("delete-bike/<int:pk>", views.staff_delete_bike, name="staff-delete-bike"),
    path("edit-bike/<int:pk>", views.staff_edit_bike, name="staff-edit-bike"),
    path(
        "mark-avaiable/<int:pk>",
        views.staff_mark_available,
        name="staff_mark_available",
    ),
]
