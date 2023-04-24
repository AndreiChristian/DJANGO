# App's urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category_list_create'),
    path('books/', views.BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]