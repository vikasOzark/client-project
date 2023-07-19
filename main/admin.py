from django.contrib import admin
from . import models


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["user", "payment_type", "colored_status", "payment_channel", "created_at"]
    date_hierarchy = "created_at"

admin.site.register(models.BankDetail)
admin.site.register(models.Payments, PaymentAdmin)
admin.site.register(models.Wallet)
