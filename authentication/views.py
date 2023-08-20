from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views import generic
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import status
from main import models as main_model
from uuid import uuid4
from django.urls import reverse
from django.http import HttpResponseNotFound

class RegisterUser(generic.TemplateView):
    template_name = "authentication/registration.html"
    
    def get_context_data(self, **kwargs):
        invite_query_param = self.request.GET
        context = super().get_context_data(**kwargs)
        
        invite_username = invite_query_param.get("user")
        invite_code = invite_query_param.get("invite_code")
        print(invite_code, invite_username)

        if all([invite_username, invite_code]):
            context["invite_username"] = invite_username
            context["invite_code"] = invite_code
            messages.info(self.request, f"Hurray !, You are invited by {invite_username}.")
            return context
        
        return context

    def post(self, request):
        form_data = request.POST
        phone_number = form_data.get("phone_number")
        
        invite_username = form_data.get("invite_username")
        invite_code = form_data.get("invite_code")

        if User.objects.filter(username=form_data.get("username")).exists():
            messages.error(request, "Username is already exists!")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST)

        if len(phone_number) != 10:
            messages.error(request, "Phone number is not valid!")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST)
        
        if phone_number != form_data.get("confirm_number"):
            messages.error(request, "Phone number is not matched!")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST )
        
        if models.UserProfileDetail.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Phone number is already exists!")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST)
        
        if models.UserProfileDetail.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Phone number is already exists!")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST )
        
        if form_data.get("password") != form_data.get("password2"):
            messages.error(request, "Password is not matched!")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST )

        new_user = User.objects.create_user(
            username=form_data.get("username"),
            password=form_data.get("password"),
            first_name=form_data.get("first_name"),
            last_name=form_data.get("last_name" ,""),
            is_active=False,
        )
        new_user.save()

        if new_user:
            uuid = str(uuid4())
            profile_obj = models.UserProfileDetail(
                user = new_user,
                phone_number=phone_number,
                invite_code=uuid[:5].upper()
            )
            profile_obj.save()
            
            if all([invite_username, invite_code]):
                user_obj = User.objects.get(username=invite_username)
                profile_obj = models.UserProfileDetail.objects.get(user = new_user)
                profile_obj.invited_user = user_obj
                profile_obj.invited_ref_code = invite_code
                profile_obj.is_invited = True
                profile_obj.save()
            
            messages.success(request, "Successfully created the account. ")
            return redirect("login")
        
        messages.error(request, "Something went wrong, Please try again!")
        return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST)
    

class Login(generic.TemplateView):
    template_name = "authentication/login.html"
    
    def post(self, request):
        form_data = request.POST
        if request.user.is_authenticated:
            return redirect("home")
        
        user = authenticate(
            request, 
            username=form_data.get("username"),
            password=form_data.get("password")
        )
        
        if user:
            login(request, user)
            messages.success(request, "Successfully logged in .")

            if user.is_superuser:
                return redirect("user-list")
            
            return redirect("home")
        else:
            messages.error(request, "Username or ID is not Matched, or account is not active.")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST)

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfuly!")
    return redirect("login")

def invite(request):
    query_params = request.GET
    user_name = query_params.get("user")
    invite_code = query_params.get("invite_code")
    
    if not all([user_name, invite_code]):
        messages.error(request, "Invite link in broken !")
        return redirect("register", permanent=True)
    
    validate_user = models.UserProfileDetail.objects.filter(
        user__username = user_name,
        invite_code = invite_code
    ).exists()
    
    if not validate_user:
        messages.error(request, "User or Invite code is not valid!")
        return redirect("register", permanent=True)
    
    register_url = reverse("register")
    return redirect(
        f"{register_url}?user={user_name}&invite_code={invite_code}",
        permanent=True
    )
    
    
    