from django.db import models
from django.utils.text import slugify


def custom_upload_to(instance, filename):
    ext = filename.split(".")[-1]  # file extension
    new_filename = f"{slugify(instance.brand)}-{slugify(instance.line)}-{slugify(instance.model)}.{ext}"
    return f"main_bike_image/{new_filename}"


class Bicycle(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    brand = models.CharField(max_length=30)  # eg Trek
    line = models.CharField(max_length=100)  # eg Slash
    model = models.CharField(max_length=30)  # eg 9.9 or SE
    generation = models.CharField(max_length=30, blank=True, null=True)  # eg gen 6
    description = models.CharField(max_length=1000)
    year_production = models.IntegerField()
    color_primary = models.CharField(max_length=30)
    color_secondary = models.CharField(max_length=30, blank=True, null=True)
    FRAME_SIZE_CHOICES: list[tuple[str, str]] = [
        ("XS", "XS"),
        ("S", "S"),
        ("S/M", "S/M"),
        ("M", "M"),
        ("M/L", "M/L"),
        ("L", "L"),
        ("XL", "XL"),
    ]
    frame_size = models.CharField(max_length=3, choices=FRAME_SIZE_CHOICES)
    FRAME_MATERIAL: list[tuple[str, str]] = [
        ("carbon", "Carbon"),
        ("steel", "Steel"),
        ("aluminium", "Aluminium"),
        ("titanium", "Titanium"),
    ]
    frame_material = models.CharField(max_length=9, choices=FRAME_MATERIAL)
    WHEEL_SIZE_CHOICES: list[tuple[str, str]] = [
        ('24"', '24"'),
        ('26"', '26"'),
        ('27.5"', '27.5"'),
        ('29"', '29"'),
    ]
    wheel_size = models.CharField(choices=WHEEL_SIZE_CHOICES, max_length=10)
    tire_size_width = models.FloatField()
    BICYCLE_PURPOSE_CHOICES: list[tuple[str, str]] = [
        ("mtb", "Mountain"),
        ("road", "Road"),
        ("gravel", "Gravel"),
        ("city", "City"),
    ]
    purpose = models.CharField(max_length=30, choices=BICYCLE_PURPOSE_CHOICES)
    # BICYCLE_CATEGORIES = []
    # category = models.CharField(max_length=30)
    suspension_front = models.BooleanField(default=True)
    suspension_back = models.BooleanField(default=True)
    weight = models.FloatField()

    is_available = models.BooleanField(default=True)
    is_serviceable = models.BooleanField(default=False)
    is_electric = models.BooleanField(default=False)
    amount = models.IntegerField(default=1)
    prize_buy = models.FloatField()
    prize_rent = models.FloatField()

    image_main = models.ImageField(default="default.png", upload_to=custom_upload_to)

    # In Issues model, in ForeignKey field related_name is set to "repair_logs"
    def get_open_repairs(self):
        return self.repair_logs.filter(is_fixed=False)  # type: ignore

    def get_total_repairs(self):
        return self.repair_logs.count()  # type: ignore

    def __str__(self) -> str:
        return f"{self.brand} {self.line} {self.model}"

    class Meta:
        ordering = ['-is_available']
