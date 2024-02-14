from django.urls import path


urlpatternss = [
        path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about")
]