from django.contrib import admin
from django.urls import include, path
from authentication import views

urlpatterns = [
    path("", include("main.urls")),
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("profile/", include("userprofile.urls")),
    path("company/", include("aboutcompany.urls")),
    path("invite/", views.invite, name="invite"),
]