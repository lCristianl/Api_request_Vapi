"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Inicializar Django
django.setup()

# Solo en Vercel, inicializar la base de datos
if os.environ.get('VERCEL') or os.environ.get('DATABASE_URL'):
    from django.core.management import call_command
    from django.db import connection
    from api_request.models import Usuario
    
    try:
        # Verificar si las tablas existen
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_name = 'api_request_usuario'
                );
            """)
            table_exists = cursor.fetchone()[0]
        
        if not table_exists:
            print("🔄 Ejecutando migraciones iniciales...")
            # Ejecutar migraciones
            call_command('migrate', '--run-syncdb', verbosity=1)
            print("✅ Migraciones completadas")
            
            # Crear usuario de prueba
            if not Usuario.objects.filter(cedula="1150334017").exists():
                Usuario.objects.create(
                    nombre="Cristian Joel Ortega Jiménez",
                    cedula="1150334017",
                    fecha_nacimiento="21/02/2005",
                    ultimos_digitos_tarjeta="2110",
                    saldo="500"
                )
                print("✅ Usuario de prueba creado")
        else:
            print("✅ Base de datos ya inicializada")
            
    except Exception as e:
        print(f"⚠️ Error inicializando base de datos: {e}")
        # Intentar ejecutar migraciones de todos modos
        try:
            call_command('migrate', verbosity=1)
            print("✅ Migraciones ejecutadas como fallback")
        except Exception as e2:
            print(f"❌ Error en fallback: {e2}")

application = get_wsgi_application()

# For Vercel deployment
app = application
