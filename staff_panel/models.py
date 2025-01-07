from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model


def custom_upload_to(instance, filename):
    ext = filename.split(".")[-1]  # file extension
    new_filename = f"{slugify(instance.brand)}-{slugify(instance.line)}-{slugify(instance.model)} issue {instance.id}.{ext}"
    return f"main_bike_image/{new_filename}"


class Issue(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    bicycle = models.ForeignKey(
        "bike_portfolio.Bicycle", on_delete=models.CASCADE, related_name="repair_logs"
    )
    issue_description = models.TextField(max_length=1000, blank=False, null=False)
    issue_image = models.ImageField(default="default.png", upload_to=custom_upload_to)
    is_fixed = models.BooleanField(default=False)

    date_reported = models.DateField(auto_now_add=True)
    reported_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reported_issues",
    )

    date_fixed = models.DateField(null=True, blank=True)
    fixed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="fixed_issues",
    )
