

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
    path('vehiculos/por_anio/<int:año>/', views.FiltrarVehiculosPorAño.as_view(), name='filtrar_vehiculos_por_anio'),
    path('vehiculos/por_precio/<str:precio>/', views.FiltrarVehiculosPorPrecio.as_view(), name='filtrar_vehiculos_por_precio'),
    path('vehiculos/por_tipo/<str:tipo_vehiculo>/', views.FiltrarVehiculosPorTipo.as_view(), name='filtrar_vehiculos_por_tipo'),
    path('vehiculos/por_anio/<int:min_año>/<int:max_año>/', views.FiltrarVehiculosPorAñoDinamico.as_view(), name='filtrar_vehiculos_por_anio'),
    path('vehiculos/por_precio/<str:min_precio>/<str:max_precio>/', views.FiltrarVehiculosPorPrecioDinamico.as_view(), name='filtrar_vehiculos_por_precio'),
]



