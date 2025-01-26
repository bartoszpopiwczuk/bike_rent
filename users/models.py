from django.db import models
from django.contrib.auth.models import AbstractUser
from bike_portfolio.models import Bicycle


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    email = models.EmailField(
        max_length=100,
        unique=True,
    )
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    adress_country = models.CharField(max_length=20, blank=True, null=True)
    adress_city = models.CharField(max_length=50, blank=True, null=True)
    adress_street = models.CharField(max_length=50, blank=True, null=True)
    adress_number = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(max_length=255, unique=True, blank=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def save(self, *args, **kwargs):
        """Automatically set the username if it's not provided"""
        if not self.username:
            super().save(*args, **kwargs)
            if self.is_staff:
                self.username = f"staff{self.id}"
            else:
                self.username = f"user{self.id}"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"User {self.first_name} {self.last_name}"


class Favourite:
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "bike")
        # each bike can be favourited once

    def __str__(self) -> str:
        return f"{self.user} - {self.bike}"
