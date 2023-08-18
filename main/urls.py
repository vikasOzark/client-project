from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", views.Home.as_view(), name="home" ),
    path("bank-account/", views.BankData.as_view(), name="add_bank"),
    path("deposit/", views.AmountDeposit.as_view(), name="deposit"),
    path("withdrawal/", views.WithdrawalView.as_view(), name="withdrawl"),
    path("teamreport/", views.TeamReport.as_view(), name="report"),
    path("task-view", views.TaskView.as_view(), name="task-view"),
    path("task-details", views.TaskDetails.as_view(), name="task-details"),
    path("profile/", include("userprofile.urls")),
]
