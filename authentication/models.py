from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class UserProfileDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # invite_code = models.CharField(max_length=5, unique=True)
    phone_number = models.CharField(max_length=15, db_index=True)

    def __str__(self) -> str:
        return f"{self.user.username} |  {self.phone_number }"
    
    # def save(self, *args, **kwargs):