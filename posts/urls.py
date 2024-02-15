from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostLiveView.as_views(), name="list"),
    path("new/", views.PostCreateView.as_views(), name="new"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="details"),
]
