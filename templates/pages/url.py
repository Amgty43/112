from django.urls import path
from .views import HOMEpageView, AboutpageView


urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]