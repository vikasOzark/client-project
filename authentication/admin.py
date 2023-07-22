from django.contrib import admin
from .models import UserProfileDetail

class HandleProfileDetail(admin.ModelAdmin):
    fields = [field.name for field in UserProfileDetail._meta.get_fields()][1:]

    readonly_fields = fields
    list_display = fields
                       

admin.site.register(UserProfileDetail, HandleProfileDetail)

# Register your models here.
