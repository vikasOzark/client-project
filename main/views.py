from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.views import generic
from . import models as main_models
from . import forms
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth.models import User
from abc import ABC, abstractmethod
from uuid import uuid4
from authentication import models as auth_model
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import AdminOnlyView, UserOnlyView, check_is_superuser


class Home(UserOnlyView, generic.TemplateView):
    template_name = "main/home.html"
    
    def get_context_data(self, **kwargs):
        user = self.request.user
        
        user_data = main_models.Wallet.objects.select_related("user").filter(user__username=user).first()
        payments = main_models.Payments.objects.filter(user=self.request.user)
        userprofile = auth_model.UserProfileDetail.objects.get(user=user)

        # Generating the invite link 
        scheme = self.request.scheme
        BASE_ADDRESS = self.request.META.get("HTTP_HOST")
        invite = reverse("invite")
        invite_link = f"{scheme}://{BASE_ADDRESS}{invite}?user={user}&invite_code={userprofile.invite_code}"

        context = super().get_context_data(**kwargs)
        context["user_data"] = user_data
        context['payments'] = payments
        context["invite_link"] = invite_link 
        return context
     

class HandlePaymentRequest(UserOnlyView, generic.CreateView):
    template_name = "main/payments.html"
    model = main_models.BankDetail
    form_class = forms.PaymentRequestForm

    def post(self, request):
        return self.get()
    
    
class BankData(UserOnlyView, generic.CreateView):
    model = main_models.BankDetail
    template_name = "main/add_bank_form.html"
    form_class = forms.AddBank
    success_url = "/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["banks"] = main_models.BankDetail.objects.filter(user = self.request.user)
        return context
	
    def form_valid(self, form):
        form_data = form.cleaned_data
        if form_data.get("account_number") != form_data.get("confirm_account"):
            messages.error(self.request, "Account Number is not matched !")
            return self.get(self.request)
            
        form.instance.user = self.request.user
        messages.success(self.request, "New bank account is added.")
        return super().form_valid(form)
    

class AmountDeposit(UserOnlyView, generic.TemplateView): 
    template_name = "main/deposit.html"


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        code = str(uuid4())
        deposit_data = main_models.Payments.objects.filter(
            user = self.request.user,
            payment_type = main_models.DEPOSIT
        )
        wallet = main_models.Wallet.objects.get(user = self.request.user)

        context = super().get_context_data(**kwargs)
        context["payment_ref_code"] = code[:10]
        context["deposit_data"] = deposit_data
        context["wallet"] = wallet
        return context

    def post(self, request):
        form_data = request.POST
        amount = form_data.get("amount")
        payment_channel = form_data.get("payment_channel")
        payment_ref_code = form_data.get("payment_ref_code")
        transaction_id = form_data.get("transaction_id")

        if not transaction_id:
            messages.error(request, "Please provide the transaction ID !")
            return self.get(request)
            
        is_transaction_id = main_models.Payments.objects.filter(user=request.user, transaction_id=transaction_id)
        if is_transaction_id.exists():
            messages.error(request, "Please valid transaction ID!")
            return self.get(request)
    
        payment_create = main_models.Payments(
                user = request.user,
                amount = amount,
                payment_channel = payment_channel,
                payment_ref = payment_ref_code,
                transaction_id = transaction_id,
                payment_type = main_models.DEPOSIT,
                payment_status = main_models.PENDING,
            )
        if payment_channel == "upi":
            payment_create.save()

        else:
            messages.success(request, "Oops !, Bank option is not Available at the moment.")
            return self.get(request)
        
        if payment_create:
            messages.success(request, "Successfully deposited, we will notify you shortly.")
            return self.get(request)

        messages.error(request, "Something went wrong , Please try again.")
        return self.get(request)
         

class WithdrawalView(UserOnlyView, generic.TemplateView):
    template_name = "main/withdraw.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        bank_accounts = main_models.BankDetail.objects.filter(user=user)
        wallet = main_models.Wallet.objects.get(user=user)
        withdrawal_data = main_models.Payments.objects.filter(
            user = self.request.user,
            payment_type = main_models.WITHDRAWAL
        )

        context = super().get_context_data(**kwargs)
        context["bank_accounts"] = bank_accounts
        context["withdrawal_data"] = withdrawal_data
        context["wallet"] = wallet
        return context
    
    def post(self, request):
        form_data = request.POST
        amount = form_data.get("amount")
        transaction_type = form_data.get("payment_channel", False)
        
        wallet = main_models.Wallet.objects.get(user=request.user)
        if int(amount) > wallet.amount:
            messages.error(request, "You have insufficient balance!")
            return self.get(request)

        if not transaction_type:
            messages.error(request, "Please select any payment method.")
            return self.get(request)
        
        if transaction_type == "UPI":
            upi_id = form_data.get("upi-id")
            upi_id_confirm = form_data.get("confirm-upi-id")
            
            if not upi_id:
                messages.error(request, "Please provide valid UPI ID.")
                return self.get(request)

            if upi_id != upi_id_confirm:
                messages.info(request, "Your UPI ID is not matched!")
                return self.get(request)
            code = str(uuid4())
            withdrawal_payment = main_models.Payments(
                user = request.user,
                amount = amount,
                payment_upi_id = upi_id,
                payment_ref = code[:10],
                payment_channel = main_models.UPI,
                payment_type = main_models.WITHDRAWAL,
                payment_status = main_models.PENDING
            )
            withdrawal_payment.save()
            messages.success(request, "Successfully withdrawal request in generated.")
            return self.get(request)
                
        else:
            bank_obj = main_models.BankDetail.objects.get(
                user=request.user,
                pk=form_data.get("bank_id")
            )
            withdrawal_payment = main_models.Payments(
                user = request.user,
                amount = amount,
                payment_channel = main_models.BANK,
                payment_type = main_models.WITHDRAWAL,
                payment_status = main_models.PENDING,
                selected_bank = bank_obj,
            )
            withdrawal_payment.save()
            messages.success(request, "Successfully withdrawal request in generated.")
            return redirect("home")
        
class TeamReport(UserOnlyView, generic.TemplateView):
    template_name = "main/message_report.html"


class TaskView(AdminOnlyView, generic.TemplateView):
    template_name = "main/task_view.html"

class TaskDetails(generic.TemplateView):
    template_name = "main/task_details.html"