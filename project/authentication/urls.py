from django.urls import path
from . import views



urlpatterns = [
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout")
]
