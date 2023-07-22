from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static
from authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("invite/", views.invite, name="invite"),
    path("", include("main.urls")),
    path("profile/", include("userprofile.urls")),
    path("company/", include("aboutcompany.urls"))
]
