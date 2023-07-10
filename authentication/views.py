from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from utils import response_format
from . import models


class RegisterUser(generic.TemplateView):
    template_name = "authentication/registration.html"

    def post(self, request):
        form_data = request.POST

        if form_data.get("password") != form_data.get("password2"):
            return render(request, self.template_name, response_format(False, 400, "Password is not matched!" ))
        if form_data.get("phone_number") != form_data.get("confrim_number"):
            return render(request, self.template_name, response_format(False, 400, "phone is not matched!" ))

        new_user = User.objects.create_user(
            username=form_data.get(""),
            first_name=form_data.get("first_name"),
            last_name=form_data.get("last_name", ""),
            email=form_data.get("email"),
        )
        new_user.save()
        new_user.set_password(form_data.get("password"))

        if new_user:
            models.UserProfileDetail.objects.create(user = new_user, phone_number=form_data.get("phone"))




        return self.get()