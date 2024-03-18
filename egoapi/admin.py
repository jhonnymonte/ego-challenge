from django.contrib import admin
from .models import Caracteristica, Color, Vehiculo





# Register your models here.

admin.site.register(Caracteristica)
admin.site.register(Color)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'marca', 'año', 'precio', 'tipo_vehiculo']
    filter_horizontal = ['caracteristicas', 'colores']
    search_fields = ['modelo', 'marca'] 
