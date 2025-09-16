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

# Solo en Vercel con SQLite, inicializar la base de datos
if os.environ.get('VERCEL') and not os.environ.get('DATABASE_URL') and not os.environ.get('DB_HOST'):
    from django.core.management import call_command
    from api_request.models import Usuario
    
    try:
        # Ejecutar migraciones
        call_command('migrate', '--run-syncdb', verbosity=0)
        
        # Crear usuario de prueba si no existe
        if not Usuario.objects.filter(cedula="1150334017").exists():
            Usuario.objects.create(
                nombre="Cristian Joel Ortega Jiménez",
                cedula="1150334017",
                fecha_nacimiento="21/02/2005",
                ultimos_digitos_tarjeta="2110",
                saldo="500"
            )
    except Exception as e:
        print(f"Error initializing database: {e}")

application = get_wsgi_application()

# For Vercel deployment
app = application
