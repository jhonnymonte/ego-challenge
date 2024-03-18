

from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from egoapi import views



urlpatterns = [
    path('crear_vehiculo/', views.CrearVehiculo.as_view(), name='crear_vehiculo'),
    path('vehiculos/', views.ListarVehiculos.as_view(), name='listar_vehiculos'),
    path('vehiculos/<int:pk>/', views.DetalleVehiculo.as_view(), name='detalle_vehiculo'),
    path('vehiculos/<int:pk>/actualizar/', views.ActualizarVehiculo.as_view(), name='actualizar_vehiculo'),
    path('vehiculos/<int:pk>/eliminar/', views.EliminarVehiculo.as_view(), name='eliminar_vehiculo'),
]

