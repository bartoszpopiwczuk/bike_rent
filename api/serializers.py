from rest_framework import serializers

from bike_portfolio.models import Bicycle
from staff_panel.models import Issue
from users.models import CustomUser, Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"


# Serializer is DRF tool that converts models to JSON
class BicycleSerializer(serializers.ModelSerializer):
    repair_logs = IssueSerializer(many=True)
    class Meta:
        model = Bicycle
        fields = "__all__"
