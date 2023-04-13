from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    # slug is a special SEO fromat that
    path("posts/<slug:slug>", views.posts_detail, name="posts-detail-page")
]
