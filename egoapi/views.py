from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vehicle
from .serializers import VehicleSerializer

class CreateVehicle(APIView):
    def post(self, request, format=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListVehicles(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleDetail(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class UpdateVehicle(generics.UpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class DeleteVehicle(generics.DestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class FilterVehiclesByYear(APIView):
    def get(self, request, year, format=None):
        vehicles = Vehicle.objects.filter(year=year)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

class FilterVehiclesByPrice(APIView):
    def get(self, request, price, format=None):
        vehicles = Vehicle.objects.filter(price=price)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

class FilterVehiclesByType(APIView):
    def get(self, request, vehicle_type, format=None):
        vehicles = Vehicle.objects.filter(vehicle_type=vehicle_type)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
    
class FilterVehiclesByDynamicYear(APIView):
    def get(self, request, min_year, max_year, format=None):
        vehicles = Vehicle.objects.filter(year__gte=min_year, year__lte=max_year)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

class FilterVehiclesByDynamicPrice(APIView):
    def get(self, request, min_price, max_price, format=None):
        vehicles = Vehicle.objects.filter(price__gte=min_price, price__lte=max_price)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
