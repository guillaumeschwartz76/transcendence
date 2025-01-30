from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from tables_core.models import Player

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
