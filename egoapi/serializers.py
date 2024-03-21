from django.db import models
from rest_framework import serializers
from .models import Vehicle, Specifications, Color

class SpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specifications
        fields = ('id', 'text', 'image')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'



class VehicleSerializer(serializers.ModelSerializer):
    colors = serializers.SerializerMethodField()
    characteristics = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = ['model', 'brand', 'price', 'image', 'vehicle_type', 'colors', 'technical_sheet', 'characteristics']

    def get_colors(self, obj):
        return [color.name for color in obj.colors.all()]

    def get_characteristics(self, obj):
        characteristics = []
        for specification in obj.specifications.all():
            characteristic_data = {
                'text': specification.text,
                'image': specification.image.url if specification.image else None
            }
            characteristics.append(characteristic_data)
        return characteristics

    def create(self, validated_data):
        characteristics_data = validated_data.pop('characteristics', [])
        colors_data = validated_data.pop('colors', [])
        vehicle = Vehicle.objects.create(**validated_data)

        for characteristic_data in characteristics_data:
            characteristic_text = characteristic_data.pop('text')
            characteristic_image = characteristic_data.pop('image', None)
            characteristic, _ = Specifications.objects.get_or_create(text=characteristic_text)
            if characteristic_image:
                characteristic.image = characteristic_image
                characteristic.save()
            vehicle.specifications.add(characteristic)

        for color_name in colors_data:
            color, _ = Color.objects.get_or_create(name=color_name)
            vehicle.colors.add(color)

        return vehicle
