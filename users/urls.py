from django.urls import path
from . import views as user_views


urlpatterns = [
    path("register/", user_views.user_register, name="user-register"),
    path("login/", user_views.user_login, name="user-login"),
    path("logout/", user_views.user_logout, name="user-logout"),
    path("add_favorite/", user_views.user_logout, name="user-logout"),
]
