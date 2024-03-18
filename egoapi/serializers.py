from django.db import models
from rest_framework import serializers
from .models import Vehiculo, Caracteristica, Color

from rest_framework import serializers
from .models import Vehiculo, Caracteristica, Color

class CaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    colores = serializers.SerializerMethodField()
    caracteristicas = serializers.SerializerMethodField()

    class Meta:
        model = Vehiculo
        fields = ['modelo', 'marca', 'precio', 'imagen', 'tipo_vehiculo', 'colores', 'ficha_tecnica', 'caracteristicas']

    def get_colores(self, obj):
        return [color.nombre for color in obj.colores.all()]

    def get_caracteristicas(self, obj):
        return [caracteristica.nombre for caracteristica in obj.caracteristicas.all()]

    def create(self, validated_data):
        caracteristicas_data = validated_data.pop('caracteristicas', [])
        colores_data = validated_data.pop('colores', [])
        vehiculo = Vehiculo.objects.create(**validated_data)

        for caracteristica_data in caracteristicas_data:
            caracteristica, _ = Caracteristica.objects.get_or_create(**caracteristica_data)
            vehiculo.caracteristicas.add(caracteristica)

        for color_nombre in colores_data:
            color, _ = Color.objects.get_or_create(nombre=color_nombre)
            vehiculo.colores.add(color)

        return vehiculo

