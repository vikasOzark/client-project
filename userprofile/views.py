from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views import generic
from main import models as main_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from authentication.models import UserProfileDetail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from utils import AdminOnlyView, UserOnlyView, check_is_superuser
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

class UserList(AdminOnlyView, generic.ListView):
    model = main_model.User
    template_name = "profile/userlist.html"
    context_object_name = "all_users"

    paginate_by = 10
    def get_queryset(self):
        queryset =  super().get_queryset()
        queryset = queryset.select_related("user_profile", "user_wallet").filter(is_superuser= False)
        return queryset
    
@login_required(login_url="login")
@user_passes_test(check_is_superuser, login_url="login")
def user_active_inactive(request):
    user_pk = request.GET.get("user")
    user = main_model.User.objects.get(pk=user_pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save(update_fields=["is_active"]) 
    return JsonResponse({"status": "deleted"})

class ProfileSettings(UserOnlyView, generic.TemplateView):
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
    
class Transactions(AdminOnlyView, generic.ListView):
    template_name = "profile/user_details.html"
    model = main_model.Payments
    context_object_name = "payments"
    paginate_by = 10


def payment_admin_view(request, pk):
    obj = main_model.Payments.objects.get(pk=pk)
    content_type = ContentType.objects.get_for_model(obj)
    change_url = reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=[obj.pk])
    return HttpResponseRedirect(change_url)