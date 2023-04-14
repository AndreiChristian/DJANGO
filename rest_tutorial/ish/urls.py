from django.urls import path
from ish import views


urlpatterns = [
    path('facilities/', views.facility_item_list),
    path('facilities/<int:pk>/', views.facility_item_detail),
]
