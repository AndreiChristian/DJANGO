from django.urls import path
from . import views

urlpatterns = [
    # dough urls
    path('doughs/', views.dough_list_create, name='dough_list_create'),
    path('doughs/<int:pk>/', views.dough_retrieve_update_destroy,
         name='dough_retrieve_update_destroy'),
    # toppings urls
    path('toppings/', views.topping_list_create, name='topping_list_create'),
    path('toppings/<int:pk>/', views.topping_retrieve_update_destroy,
         name='toppings_retrieve_update_destroy'),

    # client urls
    path('clients/', views.client_list_create, name="clien_list_create"),
    path('clients/<int:pk>/', views.client_retrieve_update_destroy,
         name="clients_retrieve_update_destroy")
]
