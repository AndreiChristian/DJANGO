from django.urls import path
from books import views

urlpatterns = [
    path('all/', views.book_list),
]