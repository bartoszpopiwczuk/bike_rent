from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser

# @receiver(post_save, sender=CustomUser)
# def autocreate_username(sender, instance, created, **kwargs):
#     print(f"Signal triggered for user: {instance}")
#     if created and not instance.username:
#         instance.username = f"user{instance.id}"
#         instance.save()
