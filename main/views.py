from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.views import generic
from . import models as main_models
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from abc import ABC, abstractmethod
from uuid import uuid4

class BaseView(ABC):
    
    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated and \
            self.request.user.is_active:
           return super().dispatch(*args, **kwargs)
       
        if not self.request.user.is_active:
            messages(self.request, "Your account is not active.")
            return redirect("login")


class Home(generic.TemplateView):
    template_name = "main/home.html"
    
    def get_context_data(self, **kwargs):
        user = self.request.user
        user_data = main_models.Wallet.objects.select_related("user").filter(user__username=user).first()
        payments = main_models.Payments.get_latest_payments(self.request)
        print(payments)
        context = super().get_context_data(**kwargs)
        context["user_data"] = user_data
        context['payments'] = payments
        return context
    
    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated and \
            self.request.user.is_active:
           return super(Home, self).dispatch(*args, **kwargs)
       
        if not self.request.user.is_active:
            messages(self.request, "Your account is not active.")
            return redirect("login")
    

class HandlePaymentRequest(generic.CreateView):
    template_name = "main/payments.html"
    model = main_models.BankDetail
    form_class = forms.PaymentRequestForm

    def post(self, request):
        print(request.POST)
        return self.get()
    
    
    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated and \
            self.request.user.is_active:
           return super(HandlePaymentRequest, self).dispatch(*args, **kwargs)
       
        if not self.request.user.is_active:
            messages(self.request, "Your account is not active.")
            return redirect("login")

class BankData(generic.CreateView):
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
        print("acount : ", form_data)
        if form_data.get("account_number") != form_data.get("confirm_account"):
            messages.error(self.request, "Account Number is not mathed !")
            return self.get(self.request)
            
        form.instance.user = self.request.user
        messages.success(self.request, "New bank account is added.")
        return super().form_valid(form)
    
    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated and \
            self.request.user.is_active:
           return super(BankData, self).dispatch(*args, **kwargs)
       
        if not self.request.user.is_active:
            messages(self.request, "Your account is not active.")
            return redirect("login")


class AmountDeposit(ABC, generic.TemplateView): 
    template_name = "main/deposit.html"


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        code = str(uuid4())
        deposit_data = main_models.Payments.objects.filter(
            user = self.request.user,
            payment_type = main_models.DEPOSIT
        )
        wallet = main_models.Wallet.objects.get(user = self.request.user)

        context = super().get_context_data(**kwargs)
        context["payment_ref_code"] = code[:8]
        context["deposit_data"] = deposit_data
        context["wallet"] = wallet
        return context

    def post(self, request):
        form_data = request.POST
        print(form_data)
        amount = form_data.get("amount")
        payment_channel = form_data.get("payment_channel")
        payment_ref_code = form_data.get("payment_ref_code")

        payment_create = main_models.Payments(
                user = request.user,
                amount = amount,
                payment_channel = payment_channel,
                payment_ref = payment_ref_code,
                payment_type = main_models.DEPOSIT,
                payment_status = main_models.PENDING,
            )
        payment_create.save()
        
        if payment_create:
            messages.success(request, "Successfully deposited, we will notify you shortly.")
            return redirect("home")

        messages.error(request, "Successfully deposited, we will notify you shortly.")
        return self.get(request)
    
    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated and \
            self.request.user.is_active:
           return super().dispatch(*args, **kwargs)
       
        if not self.request.user.is_active:
            messages(self.request, "Your account is not active.")
            return redirect("login")
        

class WithdrawalView(generic.TemplateView):
    template_name = "main/withdraw.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        bank_accounts = main_models.BankDetail.objects.filter(user=user)
        wallet = main_models.Wallet.objects.get(user=user)

        context = super().get_context_data(**kwargs)
        context["bank_accounts"] = bank_accounts
        context["wallet"] = wallet
        return context
    
    def post(self, request):
        form_data = request.POST
        print(form_data)
        
    