from django.shortcuts import redirect
from django.views import generic
from . import models as main_models
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


class Home(generic.TemplateView):
    template_name = "main/home.html"
    
    def get_context_data(self, **kwargs):
        user = self.request.user
        print(user)
        user_data = main_models.Wallet.objects.filter(user=user)
        print(user_data)
        context = super().get_context_data(**kwargs)
        context["balance_data"] = user_data
        return context
    
    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_active:
           return super(Home, self).dispatch(*args, **kwargs)
        else:
            messages(self.request, "Your account is not active.")
            return redirect("login")
    

class BankData(generic.CreateView):
    model = main_models.BankDetail
    template_name = "main/add_bank_form.html"
    form_class = forms.AddBank
	
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
