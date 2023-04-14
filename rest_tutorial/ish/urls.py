from django.urls import path
from ish import views


urlpatterns = [
    path('facilities/', views.facility_item_list),
]
