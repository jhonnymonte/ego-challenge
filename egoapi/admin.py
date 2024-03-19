from django.contrib import admin
from .models import Especificaciones, Color, Vehiculo

class ModeloConTextoImagenAdmin(admin.ModelAdmin):
    list_display = ['texto', 'imagen']

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'marca', 'año', 'precio', 'tipo_vehiculo']
    filter_horizontal = ['colores']
    search_fields = ['modelo', 'marca']

admin.site.register(Especificaciones, ModeloConTextoImagenAdmin)
admin.site.register(Color)
