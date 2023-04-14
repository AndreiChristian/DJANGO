from django.urls import path
from ish import views


urlpatterns = [
    path('facilities/group/',views.facility_group_list),
    # path('facilities/group/<int:pk>/',views.),
    path('facilities/item/', views.facility_item_list),
    # path('facilities/item/<int:pk>/', views.facility_item_detail),
]
