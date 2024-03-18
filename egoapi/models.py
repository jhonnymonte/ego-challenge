from django.db import models

class Caracteristica(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Color(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


CHOICES = [
    ('auto', 'Auto'),
    ('pickup', 'Pickup'),
    ('comercial', 'Comercial'),
    ('suv', 'SUV'),
    ('crossover', 'Crossover'),
]

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    caracteristicas = models.ManyToManyField(Caracteristica)
    colores = models.ManyToManyField(Color)
    imagen = models.ImageField(upload_to='vehiculos/')
    ficha_tecnica = models.FileField(upload_to='fichas_tecnicas/')
    tipo_vehiculo = models.CharField(
        max_length=20,
        choices=CHOICES
    )    

    def __str__(self):
        return f"{self.modelo} - {self.marca}"
