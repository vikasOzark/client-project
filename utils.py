from dataclasses import dataclass
from rest_framework import status
from abc import ABC, abstractmethod
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import logout

class AdminOnlyView(UserPassesTestMixin):
    @abstractmethod
    def test_func(self):
        # Define your custom test logic here
        user = self.request.user
        return user.is_authenticated and user.is_superuser

    @abstractmethod
    def handle_no_permission(self):        
        logout(self.request)
        messages.info(self.request, "You don't have permission.")
        return redirect("login")
    
class UserOnlyView(UserPassesTestMixin):
    @abstractmethod
    def test_func(self):
        # Define your custom test logic here
        user = self.request.user
        return user.is_authenticated and \
            not user.is_superuser and \
            not user.is_staff

    @abstractmethod
    def handle_no_permission(self):
        user = self.request.user
        if user.is_superuser and user.is_staff:
            return redirect("user-list")
        
        if user.is_authenticated:
            logout(self.request)
            messages.info(self.request, "You don't have permission. sds")
        return redirect("login")
    
def check_is_superuser(user):
    return user.is_superuser and user.is_staff