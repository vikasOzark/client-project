from typing import Any
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
        context = super().get_context_data(**kwargs)
        context["balance_data"] = user_data
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
	
    def form_valid(self, form):
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
