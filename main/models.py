from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Payments(models.Model):
    DEPOSITE = "DP"
    WITHDRAWAL = "WD"

    PAYMENT_TYPE = (
        (DEPOSITE , _('DEPOSITE')),
        (WITHDRAWAL , _('WITHDRAWAL'))
    )

    UPI = "upi"
    BANK = "bank"
    PAYMENT_CHANNEL = (
        (UPI , _("upi")),
        (BANK, _("back"))
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=25, choices=PAYMENT_TYPE)
    amount = models.CharField(max_length=10, null=False, blank=False)
    payment_channel = models.CharField(max_length=10, choices=PAYMENT_CHANNEL)
    is_settled = models.BooleanField(default=False)
    selected_bank = models.ForeignKey("BankDetail", on_delete=models.CASCADE, null=True, blank=True)
    payment_upi_id = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  db_index=True)
    amount = models.IntegerField(default=0, null=False, blank=False)
    last_updated = models.DateTimeField(auto_now_add=True)
    
class BankDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_holder_name = models.CharField(max_length=15)
    bank_name = models.CharField(max_length=15)
    ifsc_code = models.CharField(max_length=10)
    branch = models.CharField(max_length=20)
    account_number = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)