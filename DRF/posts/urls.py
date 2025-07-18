from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path("homepage/", views.homepage, name = "post homepage"),
    path("", PostListCreateView.as_view(), name = "PostListCreateView"),
    path("<int:pk>",  PostRetrieveupdateDeleteView.as_view(), name = "PostRetrieveupdateDeleteView"),
]
