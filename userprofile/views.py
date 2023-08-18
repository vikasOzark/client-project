from django.shortcuts import redirect
from django.views import generic
from main import models as main_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from authentication.models import UserProfileDetail
from django.contrib.auth.decorators import user_passes_test
from utils import AdminOnlyView, UserOnlyView, check_is_superuser
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db.models import Sum, Case, When, F
from django.db.models import DecimalField
from . import models as user_profile_model
from datetime import datetime, timedelta

class UserList(AdminOnlyView, generic.ListView):
    model = main_model.User
    template_name = "profile/userlist.html"
    context_object_name = "all_users"

    paginate_by = 10
    def get_queryset(self):
        query_params = self.request.GET.get("search_query")
        queryset =  super().get_queryset()
        query_set = queryset.select_related("user_profile", "user_wallet").filter(is_superuser= False)

        if not query_params:
            return query_set
        
        if query_params.lower() == "all":
            return query_set

        return query_set.filter(
            Q(username__icontains = query_params) |
            Q(first_name__icontains = query_params) |
            Q(email__icontains = query_params) |
            Q(user_profile__phone_number__icontains = query_params)
        ) 
    
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

    def get_queryset(self):
        query_params = self.request.GET.get("search_query")
        query_set =  super().get_queryset()

        if not query_params:
            return query_set
        
        if query_params.lower() == "all":
            return query_set

        return query_set.filter(
            Q(user__username__icontains = query_params) |
            Q(user__first_name__icontains = query_params) |
            Q(user__email__icontains = query_params) |
            Q(payment_ref__icontains = query_params)
        ) 

def payment_admin_view(request, pk):
    obj = main_model.Payments.objects.get(pk=pk)
    content_type = ContentType.objects.get_for_model(obj)
    change_url = reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=[obj.pk])
    return HttpResponseRedirect(change_url)

@require_http_methods(["POST"])    
def update_payment_status(request, pk):
    action = request.POST.get("payment_status", None)

    if action is None:
        return redirect("user-details")
    
    transaction = main_model.Payments.objects.get(pk=pk)
    if transaction.payment_status == main_model.PENDING:
        
        transaction.payment_status = action
        transaction.save(update_fields=["payment_status"])
        messages.success(request, f"Payment status is update of, {transaction.user.first_name}")
        return redirect("user-details")
    else :
        messages.success(request, f"Payment status is already updated of, {transaction.user.first_name}")
        return redirect("user-details")
    
def task_details(request):
    user = request.user
    return user_profile_model.Task.objects.filter(created_at__date = datetime.now().date(), user = user)
    
    
def profit_loss_details(request):
    user = request.user
    previous_date = datetime.today() - timedelta(days=1)
    
    result = user_profile_model.ProfitAndLoss.objects.filter(user=user)
    
    total_pnl = result.aggregate(
        total_profit=Sum(Case(When(amount_type='profit', then=F('amount')), default=0)),
        total_loss=Sum(Case(When(amount_type='loss', then=F('amount')), default=0)),
        today = Sum(Case(When(created_at__date = datetime.now().date(), amount_type='profit', then=F('amount')), default=0)),
        yesterday = Sum(Case(When(created_at__date = previous_date, amount_type='profit', then=F('amount')), default=0))
    )

    return total_pnl



class HandleTask(AdminOnlyView, generic.TemplateView):
    template_name = "main/message_report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_params = self.request.GET
        
        all_user = main_model.User.objects.filter(
            is_superuser=False, is_staff = False, is_active=False
        )
        context["all_user"] = all_user

        if user_pk := kwargs.get("user_pk", False):
            user_task = user_profile_model.Task.objects.filter(
                user__pk = user_pk,
                created_at__date = datetime.now().date()
            )
            context["user_task"] = user_task 

        if query_date := query_params.get("date"):
            user_task = user_profile_model.Task.objects.filter(
                user__pk = user_pk,
                created_at__date = query_date
            )
            context["user_task"] = user_task
        return context
    
    
    def post(self, request):
        form_data = request.POST
        task_user = main_model.User.objects.filter(pk=form_data.user_pk).first()

        if task_user:
            user_profile_model.Task.objects.create(
                user=task_user,
                task=form_data.get("task")
            )
        
            messages.success(request, f"Task is created successfully for the {task_user}")
            return self.get(request, user_pk=task_user)

def handle_task_user(request):
    form_data = request.POST
    user_obj = main_model.User.objects.get(form_data.get(""))