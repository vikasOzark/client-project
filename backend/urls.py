from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("", include("main.urls")),
    path("profile/", include("userprofile.urls"))
]
