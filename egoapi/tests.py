from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Vehiculo

class ListVehiclesTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('list_vehicles')

        image_temp = SimpleUploadedFile("toyota.jpeg", b"file_content", content_type="image/jpeg")
        technical_sheet_temp = SimpleUploadedFile("Challenge-BackEnd-Agencia-EGO.pdf", b"file_content", content_type="application/pdf")

        Vehiculo.objects.create(
            model='Corolla',
            brand='Toyota',
            year=2023,
            price='1300000.00',
            vehicle_type='auto',
            image=image_temp,
            technical_sheet=technical_sheet_temp
        )
        Vehiculo.objects.create(
            model='Hilux',
            brand='Toyota',
            year=2022,
            price='2300000.00',
            vehicle_type='auto',
            image=image_temp,
            technical_sheet=None
        )

    def test_list_vehicles(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        vehicles = response.data
        self.assertEqual(len(vehicles), 2)
        self.assertEqual(vehicles[0]['model'], 'Corolla')
        self.assertEqual(vehicles[1]['model'], 'Hilux')
