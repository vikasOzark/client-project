from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.AboutUs.as_view(), name="about" ),
    path("company_qualification/", views.CompanyQualifications.as_view(), name="company_qualification"),
    path("investment/", views.Investment.as_view(), name="investment"),
    path("notice/", views.Notice.as_view(), name="notice"),
    path("terms_condition/", views.TermsConditions.as_view(), name="terms_condition"),
]