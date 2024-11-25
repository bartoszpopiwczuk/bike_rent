from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


@receiver(signal=post_save, sender=User)
def autocreate_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(signal=post_save, sender=User)
def autosave_profile(sender, instance, **kwargs):
    instance.userprofile.save()
