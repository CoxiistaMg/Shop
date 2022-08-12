from django.db.models.signals import post_save
from account.models import User
from .models import Carrinho
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_carrinho(sender, instance, created, **kwargs):
    if created:
        Carrinho.objects.create(dono=instance)