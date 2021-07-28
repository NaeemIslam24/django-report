from . models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def profile_auto_create(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
        )
