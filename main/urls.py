from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", views.Home.as_view(), name="home" ),
    path("bank-account/", views.BankData.as_view(), name="add_bank"),
    path("deposit/", views.AmountDeposit.as_view(), name="deposit"),
    path("withdrawl/", views.WithdrawlView.as_view(), name="withdrawl"),


]
