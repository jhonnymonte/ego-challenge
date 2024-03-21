from django.urls import path
from egoapi import views

urlpatterns = [
    path('create_vehicle/', views.CreateVehicle.as_view(), name='create_vehicle'),
    path('vehicles/', views.ListVehicles.as_view(), name='list_vehicles'),
    path('vehicles/<int:pk>/', views.VehicleDetail.as_view(), name='vehicle_detail'),
    path('vehicles/<int:pk>/update/', views.UpdateVehicle.as_view(), name='update_vehicle'),
    path('vehicles/<int:pk>/delete/', views.DeleteVehicle.as_view(), name='delete_vehicle'),
    path('vehicles/by_year/<int:year>/', views.FilterVehiclesByYear.as_view(), name='filter_vehicles_by_year'),
    path('vehicles/by_price/<str:price>/', views.FilterVehiclesByPrice.as_view(), name='filter_vehicles_by_price'),
    path('vehicles/by_type/<str:vehicle_type>/', views.FilterVehiclesByType.as_view(), name='filter_vehicles_by_type'),
    path('vehicles/by_year/<int:min_year>/<int:max_year>/', views.FilterVehiclesByDynamicYear.as_view(), name='filter_vehicles_by_dynamic_year'),
    path('vehicles/by_price/<str:min_price>/<str:max_price>/', views.FilterVehiclesByDynamicPrice.as_view(), name='filter_vehicles_by_dynamic_price'),
]
