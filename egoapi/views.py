from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vehiculo
from .serializers import VehiculoSerializer


class CrearVehiculo(APIView):
    def post(self, request, format=None):
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListarVehiculos(generics.ListAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class DetalleVehiculo(generics.RetrieveAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class ActualizarVehiculo(generics.UpdateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class EliminarVehiculo(generics.DestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


class FiltrarVehiculosPorAño(APIView):
    def get(self, request, año, format=None):
        vehiculos = Vehiculo.objects.filter(año=año)
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)

class FiltrarVehiculosPorPrecio(APIView):
    def get(self, request, precio, format=None):
        vehiculos = Vehiculo.objects.filter(precio=precio)
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)

class FiltrarVehiculosPorTipo(APIView):
    def get(self, request, tipo_vehiculo, format=None):
        vehiculos = Vehiculo.objects.filter(tipo_vehiculo=tipo_vehiculo)
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)
    
class FiltrarVehiculosPorAñoDinamico(APIView):
    def get(self, request, min_año, max_año, format=None):
        vehiculos = Vehiculo.objects.filter(año__gte=min_año, año__lte=max_año)
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)

class FiltrarVehiculosPorPrecioDinamico(APIView):
    def get(self, request, min_precio, max_precio, format=None):
        vehiculos = Vehiculo.objects.filter(precio__gte=min_precio, precio__lte=max_precio)
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)