from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static
from authentication import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("", include("main.urls")),
    path("invite/", views.invite, name="invite"),
    path("profile/", include("userprofile.urls")),
    path("company/", include("aboutcompany.urls"))
]
