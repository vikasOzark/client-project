from django.urls import path
from . import views


urlpatterns = [
    path("profileSetting/", views.ProfileSettings.as_view(), name="profile-setting" ),
    path("userlist/", views.UserList.as_view(), name="user-list"),
    path("userdetails/", views.UserDetails.as_view(), name="user-details"),
]