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
           return super(Home, self).dispatch(*args, **kwargs)
       
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

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["banks"] = main_models.BankDetail.objects.filter(user = self.request.user)
        return context
	
    def form_valid(self, form):
        form_data = form.cleaned_data

        if form_data.get("account_number") != form_data.get("confirm_account"):
            messages.error(self.request, "Account Number is not mathed !")
            return self.get(self.request)
            
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated and \
            self.request.user.is_active:
           return super(BankData, self).dispatch(*args, **kwargs)
       
        if not self.request.user.is_active:
            messages(self.request, "Your account is not active.")
            return redirect("login")


class AmountDeposite(generic.TemplateView):
    template_name = "main/deposite.html"


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        code = str(uuid4())
        context = super().get_context_data(**kwargs)
        context["payment_ref_code"] = code[:8]
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
                payment_type = main_models.DEPOSITE,
                payment_status = main_models.PENDING,
            )
        payment_create.save()
        return redirect("home")
    
    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated and \
            self.request.user.is_active:
           return super(AmountDeposite, self).dispatch(*args, **kwargs)
       
        if not self.request.user.is_active:
            messages(self.request, "Your account is not active.")
            return redirect("login")
        


class WithdrawlView(generic.TemplateView):
    template_name = "main/withdraw.html"