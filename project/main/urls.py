from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", views.Home.as_view(), name="home" ),
    path("add-bank/", views.BankData.as_view(), name="add_bank")
]
