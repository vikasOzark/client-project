from django.urls import path
from . import views


urlpatterns = [
    path("profile/", views.ProfileSettings.as_view(), name="profile-setting" ),
    path("profile/", views.UserList.as_view(), name="user-list"),
]