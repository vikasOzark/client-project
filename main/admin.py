from django.contrib import admin
from . import models


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["user", "amount", "payment_type", "colored_status", "transaction_id", "payment_channel", "created_at"]
    date_hierarchy = "created_at"
    readonly_fields = ["user", "payment_type", "payment_channel", "created_at", "transaction_id",  "payment_ref", "amount", "selected_bank", "payment_upi_id", "is_settled"]
    search_fields = ["transaction_id", "amount", "user__first_name"]
    list_filter = ["payment_type", "payment_channel", 'created_at']
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super(PaymentAdmin, self).get_readonly_fields(request, obj))
        if obj and obj.payment_status == models.SUCCESS:
            readonly_fields.append("payment_status")
        return readonly_fields
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(models.Payments, PaymentAdmin)

class BankAdmin(admin.ModelAdmin):
    fields = [ "user", "account_holder_name", "bank_name", "ifsc_code", "branch", "account_number", "created_at"]
    list_display = fields
    readonly_fields = fields

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(models.BankDetail, BankAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ["user", "color_amount"]
    readonly_fields = ["user", "amount"]

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(models.Wallet, WalletAdmin)
