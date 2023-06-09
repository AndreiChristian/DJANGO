from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path("books", views.book_list),
    path("books/<int:pk>", views.book_detail),
    path("categories", views.category_list),
    path("categories/<int:pk>", views.category_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
