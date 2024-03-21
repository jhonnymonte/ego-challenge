Proyecto Django - Administración de Vehículos

Este proyecto Django proporciona una aplicación para administrar vehículos a través de una interfaz de administración y una API RESTful.

Configuración del Entorno
--
Clonar el Repositorio:

git clone <url_del_repositorio>
---
Crear un Entorno Virtual:

python3 -m venv venv
Activar el Entorno Virtual:
En Windows:
venv\Scripts\activate
##
En macOS/Linux:
source venv/bin/activate

Instalación de Dependencias:
--
pip install -r requirements.txt

Configuración de la Base de Datos:
--
Asegúrate de configurar correctamente tu base de datos en settings.py.
Aplicar Migraciones:

python manage.py migrate
Ejecución del Servidor

Para ejecutar el servidor de desarrollo, usa el siguiente comando:
--

python manage.py runserver
El servidor se ejecutará en http://127.0.0.1:8000/ por defecto.

Interfaz de Administración
--
Puedes acceder a la interfaz de administración para administrar vehículos y otras entidades utilizando las siguientes credenciales:

URL: http://127.0.0.1:8000/admin/
Usuario: <usuario_admin>
Contraseña: <contraseña_admin>
Crear un Superusuario por la Terminal

Para crear un superusuario por la terminal, usa el siguiente comando y sigue las instrucciones:
--

python manage.py createsuperuser

Crear un Vehículo a través del Admin

Inicia sesión en la interfaz de administración.
Navega a la sección de Vehículos.
Haz clic en "Agregar" para crear un nuevo vehículo.
Completa los campos requeridos, como modelo, marca, año, precio, etc.
Guarda el vehículo.
Crear un Vehículo a través de la API

Puedes crear un vehículo utilizando la API RESTful. Aquí hay un ejemplo de cómo hacerlo con cURL:


curl -X POST \
  http://localhost:8000/api/create_vehicle/ \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "Corolla",
    "brand": "Toyota",
    "year": 2023,
    "price": "1300000.00",
    "vehicle_type": "auto",
    "image": "http://localhost:8000/media/vehicles/toyota.jpeg",
    "technical_sheet": "http://localhost:8000/media/technical_sheets/Challenge_BackEnd_-_Agencia_EGO.pdf",
    "colors": ["red", "blue"],
    "specifications": [
        {
            "text": "front-wheel drive",
            "image": "http://localhost:8000/media/specifications/front_wheel_drive.jpg"
        }
    ]
}'
Uso de la API para Mostrar un Auto

Puedes utilizar la API RESTful para mostrar detalles de un vehículo específico. Aquí hay un ejemplo de cómo hacerlo:


curl -X GET http://localhost:8000/api/vehicles/<id_vehiculo>/
Reemplaza <id_vehiculo> con el ID del vehículo que deseas mostrar.

