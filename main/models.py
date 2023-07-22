from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.contrib import admin

DEPOSIT = "DEPOSIT"
WITHDRAWAL = "WITHDRAWAL"

PAYMENT_TYPE = (
    (DEPOSIT , _('DEPOSIT')),
    (WITHDRAWAL , _('WITHDRAWAL'))
)

UPI = "upi"
BANK = "bank"

PAYMENT_CHANNEL = (
    (UPI , _("upi")),
    (BANK, _("bank"))
)

PENDING = "pending"
SUCCESS = "success"
REJECTED = "rejected"

PAYMENT_STATUS = (
    (PENDING , _("pending")),
    (SUCCESS, _("success")),
    (REJECTED, _("rejected"))
)

class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_ref = models.CharField(max_length=10, default="", blank=True)
    payment_type = models.CharField(max_length=25, choices=PAYMENT_TYPE, )
    amount = models.CharField(max_length=10, null=False, blank=False)
    payment_channel = models.CharField(max_length=10, choices=PAYMENT_CHANNEL)
    payment_status = models.CharField(max_length=15, choices=PAYMENT_STATUS, default="pending")
    is_settled = models.BooleanField(default=False)
    selected_bank = models.ForeignKey("BankDetail", on_delete=models.CASCADE, null=True, blank=True)
    payment_upi_id = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by= 'created_at'

    def get_latest_payments(request, record_number:int=10, payment_type=WITHDRAWAL):
        payment_record = Payments.objects.filter(user=request.user, payment_type=payment_type)
        if len(payment_record) > 0:
            return payment_record.order_by('-id')[:record_number]
        return None
    
    def __str__(self) -> str:
        return f" {self.user}"
    
    @admin.display
    def colored_status(self):
        color = ""
        if self.payment_status == "pending":
            color = "1D5D9B"
        elif self.payment_status == "success":
            color = "1A5D1A"
        else:
            color = "F24C3D"
        
        return format_html(
            '<span style="color: #{}; font-size: medium; font-weight: 500">{}</span>',
            color,
            self.payment_status,
        )

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  db_index=True)
    amount = models.IntegerField(default=0, null=False, blank=False)
    last_updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
    
    @admin.display
    def color_amount(self):
        amount = self.amount
        return format_html(
            f"<span style='color: #1A5D1A; font-size: medium; font-weight: 500' >{amount}</span>"
        )
    
class BankDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_holder_name = models.CharField(max_length=15)
    bank_name = models.CharField(max_length=15)
    ifsc_code = models.CharField(max_length=10)
    branch = models.CharField(max_length=20)
    account_number = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return str(self.user)
    
    