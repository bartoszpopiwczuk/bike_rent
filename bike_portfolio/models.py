from django.db import models
import uuid


class Bicycle(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    brand = models.CharField(max_length=30)  # eg Trek
    line = models.CharField(max_length=100)  # eg Slash
    model = models.CharField(max_length=30)  # eg 9.9 or SE
    generation = models.CharField(max_length=30, blank=True, null=True)  # eg gen 6
    description = models.CharField(max_length=200)
    year_production = models.IntegerField()
    color_primary = models.CharField(max_length=30)
    color_secondary = models.CharField(max_length=30, blank=True, null=True)
    FRAME_SIZE_CHOICES = [
        ("XS", "XS"),
        ("S", "S"),
        ("S/M", "S/M"),
        ("M", "M"),
        ("M/L", "M/L"),
        ("L", "L"),
        ("XL", "XL"),
    ]
    frame_size = models.CharField(max_length=3, choices=FRAME_SIZE_CHOICES)
    FRAME_MATERIAL = [
        ("carbon", "Carbon"),
        ("steel", "Steel"),
        ("aluminium", "Aluminium"),
        ("titanium", "Titanium"),
    ]
    frame_material = models.CharField(max_length=30, choices=FRAME_MATERIAL)
    WHEEL_SIZE_CHOICES = [
        ("24", 24),
        ("26", 26),
        ("27.5", 27.5),
        ("29", 29),
    ]
    wheel_size = models.FloatField(choices=WHEEL_SIZE_CHOICES)
    tire_size_width = models.FloatField()
    BICYCLE_TYPES = [
        ("mtb", "Mountain"),
        ("road", "Road"),
        ("gravel", "Gravel"),
        ("city", "City"),
    ]
    type = models.CharField(max_length=30)
    # BICYCLE_CATEGORIES = []
    # category = models.CharField(max_length=30)
    suspension_front = models.BooleanField(default=True)
    suspension_back = models.BooleanField(default=True)
    weight = models.FloatField()
    prize_buy = models.FloatField()
    prize_rent = models.FloatField()
