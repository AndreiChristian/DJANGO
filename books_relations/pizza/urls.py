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
         name="clients_retrieve_update_destroy"),

    # Pizza URLs
    path('pizzas/', views.pizza_list_create, name='pizza_list_create'),
    path('pizzas/<int:pk>/', views.pizza_retrieve_update_destroy,
         name='pizza_retrieve_update_destroy'),

    # Order URLs
    path('orders/', views.order_list_create, name='order_list_create'),
    path('orders/<int:pk>/', views.order_retrieve_update_destroy,
         name='order_retrieve_update_destroy'),
]
