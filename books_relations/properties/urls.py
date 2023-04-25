from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.PropertyListCreate.as_view(),
         name='property_list_create'),
    path('properties/<int:pk>/', views.PropertyRetrieveUpdateDestroy.as_view(),
         name='property_retrieve_update_destroy'),
    path('facility_categories/', views.FacilityCategoryListCreate.as_view(),
         name='facility_category_list_create'),
    path('facility_categories/<int:pk>/', views.FacilityCategoryRetrieveUpdateDestroy.as_view(),
         name='facility_category_retrieve_update_destroy'),
    path('facility_subcategories/', views.FacilitySubCategoryListCreate.as_view(),
         name='facility_subcategory_list_create'),
    path('facility_subcategories/<int:pk>/', views.FacilitySubCategoryRetrieveUpdateDestroy.as_view(),
         name='facility_subcategory_retrieve_update_destroy'),
    path('facility_items/', views.FacilityItemListCreate.as_view(),
         name='facility_item_list_create'),
    path('facility_items/<int:pk>/', views.FacilityItemRetrieveUpdateDestroy.as_view(),
         name='facility_item_retrieve_update_destroy'),
    path('users/', views.UserListCreate.as_view()),
    path("users/<int:pk>", views.UserRetrieveUpdateDestroy.as_view()),
    path('reservations/', views.ReservationListCreate.as_view()),
    path('reservations/<int:pk>', views.ReservationRetrieveUpdateDestroy.as_view()),
]

