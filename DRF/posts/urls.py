from django.urls import path
from . import views
urlpatterns = [
    path("homepage/", views.homepage, name = "post homepage"),
    path("", views.list_posts, name = "list_posts"),
    path("<int:post_index>", views.post_detail, name = "post_detail"),
]
