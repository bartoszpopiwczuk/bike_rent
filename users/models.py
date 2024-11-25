from django.db import models
from django.contrib.auth.models import User


# exentnds User model with additional shipping information
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    adress_country = models.CharField(max_length=20, blank=True, null=True)
    adress_city = models.CharField(max_length=30, blank=True, null=True)
    adress_street = models.CharField(max_length=50, blank=True, null=True)
    adress_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name} Profile"
