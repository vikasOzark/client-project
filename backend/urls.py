from django.contrib import admin
from django.urls import include, path
from authentication import views

urlpatterns = [
    path("", include("aboutcompany.urls")),
    path("dashbord/", include("main.urls")),
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("invite/", views.invite, name="invite"),
    # path("__debug__/", include("debug_toolbar.urls")),
]