from django.shortcuts import render
from django.views import generic

# Create your views here.

class ProfileSettings(generic.TemplateView):
    template_name = "profile/profile_settings.html"


class UserList(generic.TemplateView):
    template_name = "profile/userlist.html"