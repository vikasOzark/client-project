from main import models
from django import forms

class AddBank(forms.ModelForm):
    class Meta:
        model = models.BankDetail
        fields = ["account_holder_name","bank_name","ifsc_code","branch","account_number",]
        widgets = {
            'account_holder_name': forms.TextInput(attrs={'class': 'bg-red-500'}),
            "account_holder_name" : forms.TextInput(attrs={"class" : "bg-red-500"}),
            "bank_name" : forms.TextInput(attrs={"class" : "bg-red-500"}),
            "ifsc_code" : forms.TextInput(attrs={"class" : "bg-red-500"}),
            "branch" : forms.TextInput(attrs={"class" : "bg-red-500"}),
            "account_number" : forms.TextInput(attrs={"class" : "bg-red-500"}),
            }
	