from django.urls import path

from . import views as user_views

urlpatterns = [
    path("register/", user_views.user_register, name="user-register"),
    path("login/", user_views.user_login, name="user-login"),
    path("logout/", user_views.user_logout, name="user-logout"),
    path("add_favorite/<str:pk>", user_views.toggle_favorite, name="user-toggle-favorites"),
    path("my_favorites/", user_views.my_favorites, name="user-my-favorites"),
]
