from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


PROFIT = "profit"
LOSS = "loss"

AMOUNT_TYPE = (
    (PROFIT, _("profit")),
    (LOSS, _("loss"))
)

class ProfitAndLoss(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    amount_type = models.CharField(max_length=40, choices=AMOUNT_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.amount} | {self.amount_type}"
    
COMPLETE = "complete"
PENDING = "pending"

TASK_STATUS = (
    (COMPLETE, _("complete")),
    (PENDING, _("pending"))
)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    task_status = models.CharField(max_length=50, choices=TASK_STATUS, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    
    