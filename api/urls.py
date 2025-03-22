from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("users/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", views.getRoutes),
    path("bicycles", views.getBicycles),
    path(
        "bicycle/<str:pk>/", views.getBicycle
    ),  # it's better to pass id as type:str, because id can often contain letters eg. UUID
    path("bicycle/<str:pk>/add-issue", views.addIssue),
]
