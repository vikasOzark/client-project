from main import models
from django import forms

class AddBank(forms.ModelForm):
    confirm_account = forms.CharField()
    class Meta:
        model = models.BankDetail
        fields = ["account_holder_name","bank_name","ifsc_code","branch","confirm_account" ,"account_number",]
        css = "border pl-12 h-12 border-gray-500 rounded text-slate-500 font-medium tracking-wide text-sm focus:outline-none block w-full p-2"
        widgets = {
            'account_holder_name': forms.TextInput(attrs={'class': css}),
            "bank_name" : forms.TextInput(attrs={"class" : css}),
            "ifsc_code" : forms.TextInput(attrs={"class" : css}),
            "branch" : forms.TextInput(attrs={"class" : css}),
            "account_number" : forms.PasswordInput(attrs={"class" : css}),
            "confirm_account" : forms.TextInput(attrs={"class" : css}),
            }
 
class PaymentRequestForm(forms.ModelForm):
    selected_bank = forms.ModelChoiceField(queryset=models.BankDetail.objects.all(), required=False)
    class Meta:
        model = models.Payments
        fields = ["selected_bank","amount","payment_channel","payment_upi_id"]