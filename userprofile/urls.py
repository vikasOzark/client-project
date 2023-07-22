from django.urls import path
from . import views


urlpatterns = [
    path("profileSetting/", views.ProfileSettings.as_view(), name="profile-setting" ),
    path("userlist/", views.UserList.as_view(), name="user-list"),
    path("delete-bank/<int:pk>", views.delete_bank_account, name="delete-bank"),
    path("change-password/", views.change_password, name="change-passowrd")
]