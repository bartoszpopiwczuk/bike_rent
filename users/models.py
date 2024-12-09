from django.db import models
from django.contrib.auth.models import AbstractUser


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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    def save(self, *args, **kwargs):
        # Automatically set the username if it's not provided
        if not self.username:
            # Use the id after the object is saved for the first time
            super().save(*args, **kwargs)  # Save to generate an id
            self.username = f"user{self.id}"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"User {self.first_name} {self.last_name}"
