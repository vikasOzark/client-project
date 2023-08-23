from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="webhome"),
    path("about/", views.AboutUs.as_view(), name="about" ),
    path("work-from-home/", views.CompanyQualifications.as_view(), name="work_from_home"),
    path("terms-condition/", views.TermsConditions.as_view(), name="terms_condition"),
]