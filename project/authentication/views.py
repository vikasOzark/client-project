from django.shortcuts import render, redirect
from django.views import generic
from utils import response_format
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework import status

class RegisterUser(generic.TemplateView):
    template_name = "authentication/registration.html"

    def post(self, request):
        form_data = request.POST
        
        if (User.objects.filter(username=form_data.get("username"))):
            messages.error(request, "Username is already exists!")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST)

        if (models.UserProfileDetail.objects.filter(phone_number=form_data.get("phone_number"))):
            messages.error(request, "Phone number is already exists!")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST )
        
        if form_data.get("password") != form_data.get("password2"):
            messages.error(request, "Password is not matched!")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST )

        if form_data.get("phone_number") != form_data.get("confirm_number"):
            messages.error(request, "Phone number is not matched!")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST )

        new_user = User.objects.create_user(
            username=form_data.get("username"),
            password=form_data.get("password"),
            first_name=form_data.get("first_name"),
            last_name=form_data.get("last_name" ,"")
        )
        if new_user:
            user_profile = models.UserProfileDetail.objects.create(
                user = new_user, 
                phone_number=form_data.get("phone_number"))
            user_profile.save()
            new_user.save()

        if new_user:
            user_profile = models.UserProfileDetail.objects.create(
                user = new_user, 
                phone_number=form_data.get("phone_number"))
            user_profile.save()
        is_user = authenticate(
            request, username=form_data.get("username"),
            password=form_data.get("password")
        )

        if is_user:
            login(request, is_user)

            messages.success(request, "Successfully logged in. ")
            return
        
        messages.error(request, "Something went wrong, Please try again!")
        return render(request, self.template_name, response_format(False, 201, "Successfully Login User."))
    

class Login(generic.TemplateView):
    template_name = "authentication/login.html"
    
    def post(self, request):
        form_data = request.POST
        print(form_data)
        if(request.user.is_authenticated):
            print('======================')
            return 
        
        user = authenticate(
            request, 
            username=form_data.get("username"),
            password=form_data.get("password")
        )
        if user:
            login(request, user)
            messages.success(request, "Successfully logged in .")
            return render(request, self.template_name)
        else:
            messages.error(request, "Username or ID is not Matched !")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST)
        
        # return render(request, self.template_name)