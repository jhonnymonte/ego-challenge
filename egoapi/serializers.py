from django.db import models
from rest_framework import serializers
from .models import Vehiculo, Especificaciones, Color

class EspecificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especificaciones
        fields = ('id', 'texto', 'imagen')


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
        caracteristicas = []
        for especificacion in obj.especificaciones.all():
            caracteristica_data = {
                'texto': especificacion.texto,
                'imagen': especificacion.imagen.url if especificacion.imagen else None
            }
            caracteristicas.append(caracteristica_data)
        return caracteristicas

    def create(self, validated_data):
        caracteristicas_data = validated_data.pop('caracteristicas', [])
        colores_data = validated_data.pop('colores', [])
        vehiculo = Vehiculo.objects.create(**validated_data)

        for caracteristica_data in caracteristicas_data:
            caracteristica_texto = caracteristica_data.pop('texto')
            caracteristica_imagen = caracteristica_data.pop('imagen', None)
            caracteristica, _ = Especificaciones.objects.get_or_create(texto=caracteristica_texto)
            if caracteristica_imagen:
                caracteristica.imagen = caracteristica_imagen
                caracteristica.save()
            vehiculo.especificaciones.add(caracteristica)

        for color_nombre in colores_data:
            color, _ = Color.objects.get_or_create(nombre=color_nombre)
            vehiculo.colores.add(color)

        return vehiculo
