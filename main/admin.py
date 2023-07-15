from django.contrib import admin
from . import models


admin.site.register(models.BankDetail)
admin.site.register(models.Payments)
admin.site.register(models.Wallet)
