from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from utils import ResponseFormat


class RegisterUser(generic.TemplateView):
    template_name = "authentication/registration.html"

    def post(self, request):
        form_data = request.POST

        if form_data.get("password") != form_data.get("password2"):
            return render(request, self.template_name, ResponseFormat(False, 400, "Password is not matched!" ))

        new_user = User.objects.create_user(
            username=form_data.get(""),
            first_name=form_data.get("first_name"),
            last_name=form_data.get("last_name"),
            email=form_data.get("email"),
        )

        return self.get()