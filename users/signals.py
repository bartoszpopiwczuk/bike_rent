from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=User)
def autocreate_username(sender, instance, created, **kwargs):
    print(f"Signal triggered for user: {instance}")
    if created and not instance.username:
        instance.username = f"user{instance.id}"
        instance.save()


@receiver(signal=post_save, sender=User)
def autocreate_profile(sender, instance, created, **kwargs):
    print(f"Signal triggered for user: {instance}")
    if created:
        UserProfile.objects.create(user=instance)


@receiver(signal=post_save, sender=User)
def autosave_profile(sender, instance, **kwargs):
    print(f"Signal triggered for user: {instance}")
    if hasattr(instance, "profile"):
        instance.profile.save()
