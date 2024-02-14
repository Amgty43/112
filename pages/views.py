from django.shortcuts import render

# Create your views here.
class HomepageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"