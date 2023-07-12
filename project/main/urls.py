from django.urls import path
from . import views


urlpatterns = [
    path("", views.Home.as_view(), name="home" ),
    path("add-bank/", views.BankData.as_view(), name="add_bank")
]
