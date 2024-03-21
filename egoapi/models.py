from django.db import models

class Specifications(models.Model):
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='characteristics/',null=True)

    def __str__(self):
        return self.text

class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


CHOICES = [
    ('auto', 'Auto'),
    ('pickup', 'Pickup'),
    ('commercial', 'Commercial'),
    ('suv', 'SUV'),
    ('crossover', 'Crossover'),
]

class Vehicle(models.Model):
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    specifications = models.ManyToManyField(Specifications)
    colors = models.ManyToManyField(Color)
    image = models.ImageField(upload_to='vehicles/')
    technical_sheet = models.FileField(upload_to='technical_sheets/')
    vehicle_type = models.CharField(
        max_length=20,
        choices=CHOICES
    )

    def __str__(self):
        return f"{self.model} - {self.brand}"
