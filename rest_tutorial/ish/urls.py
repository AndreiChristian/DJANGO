from django.urls import path
from ish import views


urlpatterns = [
    path('facilities/category/', views.facility_category_list),
    path('facilities/category/<int:pk>/', views.facility_category_detail),
    path('facilities/group/', views.facility_group_list),
    # path('facilities/group/<int:pk>/',views.),
    path('facilities/item/', views.facility_item_list),
    # path('facilities/item/<int:pk>/', views.facility_item_detail),
]
