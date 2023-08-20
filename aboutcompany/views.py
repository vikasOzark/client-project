from django.shortcuts import render
from django.views import generic

# Create your views here.


class AboutUs(generic.TemplateView):
    template_name = "about_company/about.html"

class Home(generic.TemplateView):
    template_name = "about_company/index.html"

class CompanyQualifications(generic.TemplateView):
    template_name = "about_company/company_qualification.html"

class Investment(generic.TemplateView):
    template_name = "about_company/investment.html"

class Notice(generic.TemplateView):
    template_name = "about_company/notice.html"

class TermsConditions(generic.TemplateView):
    template_name = "about_company/terms_condition.html"