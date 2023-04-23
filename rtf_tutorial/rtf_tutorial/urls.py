# """
# URL configuration for rtf_tutorial project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('pizzaria'),
#     path('', include('snippets.urls')),
#     path('admin/', admin.site.urls),

# ]

# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]

from django.urls import path, include
from rest_framework import routers

from pizzaria.views import OrderViewSet, PizzaViewSet, ToppingViewSet

router = routers.DefaultRouter()
router.register("orders", OrderViewSet, "orders")
router.register("pizzas", PizzaViewSet, "pizzas")
router.register("toppings", ToppingViewSet, "toppings")

urlpatterns = [
    path("pizzaria/", include(router.urls))
]
