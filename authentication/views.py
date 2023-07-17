from django.shortcuts import render, redirect
from django.views import generic
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import status
from main import models as main_model


class RegisterUser(generic.TemplateView):
    template_name = "authentication/registration.html"

    def post(self, request):
        form_data = request.POST
        print(form_data)
        phone_number = form_data.get("phone_number")

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
            models.UserProfileDetail.objects.create(
                user = new_user,
                phone_number=phone_number)
            
            main_model.Wallet.objects.create(
                user = new_user
            ).save()
            
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
            return redirect("home")
        else:
            messages.error(request, "Username or ID is not Matched, or account is not active.")
            return render(request, self.template_name, status=status.HTTP_400_BAD_REQUEST)

def logout_view(request):
    logout(request)
    return redirect("login")