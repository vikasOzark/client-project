from django.contrib import admin
from . import models

admin.site.register(models.ProfitAndLoss)


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fields = [ "user", "task", "task_status", "created_at"]
    list_display = fields
    readonly_fields = fields

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(models.Task, TaskAdmin)