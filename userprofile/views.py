from django.shortcuts import render, redirect
from django.views import generic
from main import models as main_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from authentication.models import UserProfileDetail


class UserList(generic.TemplateView):
    template_name = "profile/userlist.html"

class ProfileSettings(generic.TemplateView):
    template_name = "profile/profile_settings.html"
    

    def get_context_data(self):
        user_profile = UserProfileDetail.objects.get(user=self.request.user)
        context = super().get_context_data()
        context["user_profile"] = user_profile
        return context
    

    def post(self, request):
        form_data = request.POST
        full_name = form_data.get("full_name")
        email = form_data.get("email")

        user_obj = main_model.User.objects.get(username=request.user)
        if full_name:
            user_obj.first_name = full_name
        if email:
            user_obj.email = email
        user_obj.save(update_fields=["email", "first_name"])

        phone_number = form_data.get("phone_number")

        if phone_number:
            user_profile = UserProfileDetail.objects.get(user=request.user)
            user_profile.phone_number = phone_number
            user_profile.save(update_fields=["phone_number"])

        messages.success(request, "You profile info is updated successfull.")
        return redirect("home")



        

@login_required(login_url="login")
def delete_bank_account(request, pk):
    main_model.BankDetail.objects.get(user=request.user, pk=pk).delete()
    messages.success(request, "Successfully bank account removed.")
    return redirect("home")

@login_required(login_url="login")
@require_http_methods(["POST"])
def change_password(request):
    form_data = request.POST

    if not form_data.get("new_password") == form_data.get("confirm_new_password"):
        messages.error(request, "Your provided passowrd is not matched.")
        return redirect("profile-setting")

    is_authenticate = authenticate(request,
        username=request.user,
        password=form_data.get("old_password")
    )

    if not is_authenticate:
        messages.error(request, "Your old passowrd is incorrect.")
        return redirect("profile-setting")
    
    user = main_model.User.objects.get(username=request.user)
    user.set_password(form_data.get("confirm_new_password"))
    user.save()
    messages.success(request, "Your password is changed successfully.")    
    return redirect("login")
    