from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication import models as auth_models
from uuid import uuid4
from django.contrib.auth.models import User
from . import models as main_models


@receiver(post_save, sender=auth_models.User)
def handle_wallet_create(sender, instance, created, **kwargs):
    if created:
        main_models.Wallet.objects.create(
            user = instance
        )
        
@receiver(post_save, sender=main_models.Payments)
def handle_wallet_update(sender, instance, created, **kwargs):
    model_obj = main_models.Payments.objects.get(pk=instance.pk)
    wallet = main_models.Wallet.objects.get(user=model_obj.user)
    
    if not created and model_obj.payment_status == main_models.SUCCESS \
        and not model_obj.is_settled:
        
        if model_obj.payment_type == main_models.DEPOSIT:
            wallet.amount = wallet.amount + int(model_obj.amount)
            wallet.save()

        if model_obj.payment_type == main_models.WITHDRAWAL:
            if int(wallet.amount) > int(model_obj.amount):
                print(int(wallet.amount))
                print( int(model_obj.amount))
                wallet.amount = wallet.amoun - int(model_obj.amount)
                wallet.save()
        
        if not model_obj.is_settled:
            model_obj.is_settled = True
            model_obj.save()

        