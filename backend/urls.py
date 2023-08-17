from django.contrib import admin
from django.urls import include, path
from authentication import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("aboutcompany.urls")),
    path("dashbord/", include("main.urls")),
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("invite/", views.invite, name="invite"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)