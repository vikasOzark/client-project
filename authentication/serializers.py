from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        modal = User
        fields = ["first_name", "last_name", "email"]