from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class UserProfileDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    invite_code = models.CharField(max_length=10, unique=True, blank=True)
    invited_ref_code = models.CharField(max_length=10, blank=True)
    invited_user = models.ForeignKey(User,max_length=20, null=True, on_delete=models.CASCADE, related_name="invited_by")
    is_invited = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, db_index=True)

    def __str__(self) -> str:
        return f"{self.user.username} |  {self.phone_number }"
