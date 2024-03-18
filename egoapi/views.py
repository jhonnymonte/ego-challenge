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