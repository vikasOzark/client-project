from django.contrib import admin
from django.contrib.auth.models import Group
from . import models

admin.site.unregister(Group)
# admin.site.site_header  =  "Custom bookstore admin"  
# admin.site.site_title  =  "Custom bookstore admin site"
# admin.site.index_title  =  "Custom Bookstore Admin"


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["user", "amount", "payment_type", "colored_status", "payment_channel", "created_at"]
    date_hierarchy = "created_at"
    readonly_fields = ["user", "payment_type", "payment_channel", "created_at", "payment_ref", "amount", "selected_bank", "payment_upi_id", "is_settled"]
    list_filter = ("user", "payment_type", "payment_channel")
    search_fields = ("user__first_name__startswith", )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super(PaymentAdmin, self).get_readonly_fields(request, obj))
        if obj and obj.payment_status == models.SUCCESS:
            readonly_fields.append("payment_status")

        return readonly_fields

admin.site.register(models.Payments, PaymentAdmin)

class BankAdmin(admin.ModelAdmin):
    fields = [ "user", "account_holder_name", "bank_name", "ifsc_code", "branch", "account_number", "created_at"]
    list_display = fields
    readonly_fields = fields

admin.site.register(models.BankDetail, BankAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ["user", "color_amount"]
    readonly_fields = ["user", "amount"]

admin.site.register(models.Wallet, WalletAdmin)
