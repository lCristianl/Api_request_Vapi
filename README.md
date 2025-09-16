# API de Usuarios - Django REST Framework

Una API REST construida con Django para gestionar datos de usuarios, diseñada para ser desplegada en Vercel y usar con Supabase.

## 🚀 Características

- ✅ API REST con Django REST Framework
- ✅ Búsqueda de usuarios por cédula
- ✅ Respuestas en formato JSON estandarizado
- ✅ Configuración para CORS
- ✅ Lista para despliegue en Vercel
- ✅ Compatible con Supabase como base de datos

## 📋 Endpoints

### POST `/api/usuarios/`

Busca un usuario por su número de cédula.

**Request Body:**
```json
{
    "cedula": "1150334017"
}
```

**Response (Usuario encontrado):**
```json
{
  "data": {
    "nombre": "Cristian Joel Ortega Jiménez",
    "cedula": "1150334017",
    "fechaNacimiento": "21/02/2005",
    "ultimosDigitosTarjeta": "2110",
    "saldo": "500"
  },
  "estatus": "exitoso"
}
```

**Response (Usuario no encontrado):**
```json
{
  "data": "",
  "estatus": "exitoso"
}
```

**Response (Error - cédula faltante):**
```json
{
  "data": "",
  "estatus": "error",
  "mensaje": "La cédula es requerida"
}
```

## 🛠️ Configuración Local

### Prerrequisitos
- Python 3.8+
- pip

### Instalación

1. **Clonar el repositorio:**
```bash
git clone <tu-repositorio>
cd Api_request_Vapi
```

2. **Crear y activar entorno virtual:**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Ejecutar migraciones:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear datos de prueba (opcional):**
```bash
python manage.py shell
```
Luego ejecutar:
```python
from api_request.models import Usuario
Usuario.objects.create(
    nombre="Cristian Joel Ortega Jiménez",
    cedula="1150334017",
    fecha_nacimiento="21/02/2005",
    ultimos_digitos_tarjeta="2110",
    saldo="500"
)
exit()
```

6. **Ejecutar servidor de desarrollo:**
```bash
python manage.py runserver
```

La API estará disponible en: `http://127.0.0.1:8000/api/usuarios/`

## 🚀 Despliegue en Vercel

### Preparación

1. **Asegúrate de tener estos archivos:**
   - `vercel.json` ✅
   - `requirements.txt` ✅
   - `backend/settings_prod.py` ✅

2. **Instalar Vercel CLI:**
```bash
npm i -g vercel
```

3. **Inicializar proyecto en Vercel:**
```bash
vercel login
vercel --prod
```

### Variables de Entorno en Vercel

En el dashboard de Vercel, configura estas variables:

```
DJANGO_SETTINGS_MODULE = backend.settings_prod
PYTHONPATH = .
```

### Configuración con Supabase

1. **Crear proyecto en Supabase**
2. **Obtener credenciales de la base de datos**
3. **Agregar variables de entorno en Vercel:**

```
DB_NAME = tu_base_de_datos
DB_USER = tu_usuario
DB_PASSWORD = tu_contraseña
DB_HOST = tu_host_supabase
DB_PORT = 5432
```

4. **Descomentar la configuración de PostgreSQL en `backend/settings_prod.py`**

5. **Instalar psycopg2 para PostgreSQL:**
```bash
pip install psycopg2-binary
```

6. **Actualizar requirements.txt:**
```
Django==5.2.3
djangorestframework==3.15.2
django-cors-headers==4.7.0
psycopg2-binary==2.9.9
```

## 🧪 Pruebas

### Prueba Local
```bash
python test_api.py
```

### Prueba con cURL
```bash
# Usuario existente
curl -X POST http://127.0.0.1:8000/api/usuarios/ \
  -H "Content-Type: application/json" \
  -d '{"cedula": "1150334017"}'

# Usuario inexistente
curl -X POST http://127.0.0.1:8000/api/usuarios/ \
  -H "Content-Type: application/json" \
  -d '{"cedula": "9999999999"}'
```

## 📁 Estructura del Proyecto

```
Api_request_Vapi/
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── settings_prod.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── api_request/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Modelo Usuario
│   ├── serializers.py     # Serializer para API
│   ├── views.py          # Vista API
│   ├── urls.py           # URLs de la app
│   ├── tests.py
│   └── migrations/
├── manage.py
├── requirements.txt
├── vercel.json
├── test_api.py           # Script de pruebas
└── README.md
```

## 🔧 Modelo de Datos

**Usuario:**
- `nombre`: CharField(200) - Nombre completo
- `cedula`: CharField(20, unique=True) - Número de cédula
- `fecha_nacimiento`: CharField(10) - Fecha de nacimiento (dd/mm/yyyy)
- `ultimos_digitos_tarjeta`: CharField(4) - Últimos 4 dígitos de tarjeta
- `saldo`: CharField(20) - Saldo disponible

## 📝 Notas

- La API usa POST en lugar de GET para recibir la cédula en el body
- Todas las respuestas incluyen el campo `estatus`
- Los errores devuelven códigos HTTP apropiados
- CORS está habilitado para desarrollo y producción
- La configuración de producción está separada para mayor seguridad

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.