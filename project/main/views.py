from django.shortcuts import render
from django.views import generic
from . import models as main_models


# Create your views here.
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
    

class BankData(generic.CreateView):
    model = main_models.BankDetail
    fields = ["user","account_holder_name","bank_name","ifsc_code","branch","account_number",]


    
    
