from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models as auth_models

from uuid import uuid4
from django.contrib.auth.models import User


# @receiver(post_save, sender=User)
# def handleUserProfile(sender, instance, created,  **kwargs):
#     if created:
#         uuid = str(uuid4())
#         profile_obj = auth_models.UserProfileDetail(
#             user = instance,
#             phone_number=phone_number,
#             invite_code=uuid[:6].upper()
#         )
#         profile_obj.save()