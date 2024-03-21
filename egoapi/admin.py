from django.contrib import admin
from .models import Specifications, Color, Vehicle

class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ['text', 'image']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['model', 'brand', 'year', 'price', 'vehicle_type']
    filter_horizontal = ['colors']
    search_fields = ['model', 'brand']

admin.site.register(Specifications, SpecificationsAdmin)
admin.site.register(Color)
