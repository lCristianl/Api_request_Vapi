#!/usr/bin/env python
"""
Script para inicializar la base de datos en Vercel.
Este script se ejecuta automáticamente en cada despliegue.
"""
import os
import django
from django.core.management import call_command

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

# Ejecutar migraciones
call_command('migrate', '--run-syncdb')

# Crear usuario de prueba si no existe
from api_request.models import Usuario

if not Usuario.objects.filter(cedula="1150334017").exists():
    Usuario.objects.create(
        nombre="Cristian Joel Ortega Jiménez",
        cedula="1150334017",
        fecha_nacimiento="21/02/2005",
        ultimos_digitos_tarjeta="2110",
        saldo="500"
    )
    print("Usuario de prueba creado exitosamente")
else:
    print("Usuario de prueba ya existe")

print("Base de datos inicializada correctamente")