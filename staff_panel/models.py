from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


def custom_upload_to(instance, filename):
    ext = filename.split(".")[-1]  # file extension
    new_filename = f"{slugify(instance.bicycle.brand)}-{slugify(instance.bicycle.line)}-{slugify(instance.bicycle.model)}-issue-nr-{instance.id}.{ext}"
    return f"staff_issue_image/{new_filename}"


class Issue(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    bicycle = models.ForeignKey(
        "bike_portfolio.Bicycle", on_delete=models.CASCADE, related_name="repair_logs"
    )
    issue_description = models.TextField(max_length=1000, blank=False, null=False)
    issue_image = models.ImageField(
        default="default.png", upload_to=custom_upload_to, blank=True, null=True
    )
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

    def save(self, *args, **kwargs):
        try:
            this = Issue.objects.get(id=self.id)
            if (
                this.issue_image != self.issue_image
                and this.issue_image.name != "default.png"
            ):
                this.issue_image.delete(save=False)
        except Issue.DoesNotExist:
            pass
        super().save(*args, **kwargs)
