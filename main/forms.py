from main import models
from django import forms

class AddBank(forms.ModelForm):
    class Meta:
        model = models.BankDetail
        fields = ["account_holder_name","bank_name","ifsc_code","branch","account_number",]
        css = "w-full rounded border px-2 py-1"
        widgets = {
            'account_holder_name': forms.TextInput(attrs={'class': css}),
            "bank_name" : forms.TextInput(attrs={"class" : css}),
            "ifsc_code" : forms.TextInput(attrs={"class" : css}),
            "branch" : forms.TextInput(attrs={"class" : css}),
            "account_number" : forms.TextInput(attrs={"class" : css}),
            }
 
class PaymentRequestForm(forms.ModelForm):
    selected_bank = forms.ModelChoiceField(queryset=models.BankDetail.objects.all(), required=False)
    class Meta:
        model = models.Payments
        fields = ["selected_bank","amount","payment_channel","payment_upi_id"]