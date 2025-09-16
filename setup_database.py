#!/usr/bin/env python
"""
Script para configurar la base de datos Supabase.
Ejecuta las migraciones y crea el usuario de prueba.
"""
import os
import sys
import django

# Agregar el proyecto al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.core.management import call_command
from api_request.models import Usuario

def setup_database():
    print("🔄 Configurando base de datos Supabase...")
    
    try:
        # Ejecutar migraciones
        print("📦 Ejecutando migraciones...")
        call_command('makemigrations', verbosity=1)
        call_command('migrate', verbosity=1)
        
        # Crear usuario de prueba
        print("👤 Creando usuario de prueba...")
        if not Usuario.objects.filter(cedula="1150334017").exists():
            Usuario.objects.create(
                nombre="Cristian Joel Ortega Jiménez",
                cedula="1150334017",
                fecha_nacimiento="21/02/2005",
                ultimos_digitos_tarjeta="2110",
                saldo="500"
            )
            print("✅ Usuario de prueba creado exitosamente")
        else:
            print("ℹ️  Usuario de prueba ya existe")
        
        print("🎉 ¡Base de datos configurada correctamente!")
        
    except Exception as e:
        print(f"❌ Error configurando la base de datos: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = setup_database()
    if success:
        print("\n🚀 La base de datos está lista para usar!")
    else:
        print("\n💥 Hubo un error configurando la base de datos.")
        sys.exit(1)