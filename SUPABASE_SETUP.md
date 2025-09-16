# 🗃️ Configuración de Supabase para la API

## 📋 Pasos para Configurar Supabase

### 1. **Crear Proyecto en Supabase**

1. Ve a [supabase.com](https://supabase.com)
2. Haz clic en **"Start your project"** → **"New Project"**
3. Configura tu proyecto:
   - **Name**: `Api_request_Vapi`
   - **Database Password**: Crea una contraseña segura (¡GUÁRDALA!)
   - **Region**: Elige la más cercana
4. Haz clic en **"Create new project"**
5. Espera 2-3 minutos a que se cree

### 2. **Obtener Credenciales de la Base de Datos**

Una vez creado el proyecto:

1. Ve a **Settings** → **Database**
2. Busca la sección **"Connection parameters"**
3. Anota estos datos:

```
Host: db.xxxxxxxxxxxxxxxxx.supabase.co
Database name: postgres
Port: 5432
User: postgres
Password: [la que creaste]
```

**O usa la Connection String directamente:**
```
postgresql://postgres:[TU_PASSWORD]@db.xxxxxxxxxxxxxxxxx.supabase.co:5432/postgres
```

### 3. **Configurar Variables de Entorno en Vercel**

Ve a tu proyecto en [vercel.com](https://vercel.com):

1. **Project** → **Settings** → **Environment Variables**
2. **Agrega estas variables:**

#### **Opción A: Using Connection String (Recomendado)**
```
DATABASE_URL = postgresql://postgres:[TU_PASSWORD]@db.xxxxxxxxxxxxxxxxx.supabase.co:5432/postgres
```

#### **Opción B: Variables separadas**
```
DB_NAME = postgres
DB_USER = postgres
DB_PASSWORD = [tu_password]
DB_HOST = db.xxxxxxxxxxxxxxxxx.supabase.co
DB_PORT = 5432
```

3. **Variables adicionales:**
```
DJANGO_SETTINGS_MODULE = backend.settings
VERCEL = 1
```

### 4. **Configurar Localmente para Pruebas**

Para probar localmente con Supabase, crea un archivo `.env` en la raíz del proyecto:

```bash
# .env
DATABASE_URL=postgresql://postgres:[TU_PASSWORD]@db.xxxxxxxxxxxxxxxxx.supabase.co:5432/postgres
```

### 5. **Ejecutar Migraciones**

Una vez configuradas las variables:

```bash
# Activar entorno virtual
C:\Users\DELL\Desktop\Api_request_Vapi\venv\Scripts\activate

# Configurar variable de entorno local (Windows)
set DATABASE_URL=postgresql://postgres:[TU_PASSWORD]@db.xxxxxxxxxxxxxxxxx.supabase.co:5432/postgres

# Ejecutar script de configuración
python setup_database.py
```

### 6. **Redesplegar en Vercel**

```bash
git add .
git commit -m "Configure Supabase database"
git push origin main
```

Vercel redesplegará automáticamente con la nueva configuración.

## 🧪 **Probar la API**

Una vez desplegado, prueba tu endpoint:

**URL**: `https://tu-proyecto.vercel.app/api/usuarios/`

**POST Request**:
```json
{
    "cedula": "1150334017"
}
```

**Response esperada**:
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

## 🔧 **Verificar en Supabase**

1. Ve a tu proyecto en Supabase
2. **Table Editor** → Deberías ver la tabla `api_request_usuario`
3. Verifica que el usuario de prueba esté creado

## ⚠️ **Importante**

- **NUNCA** commits el archivo `.env` al repositorio
- Asegúrate de que `.env` esté en tu `.gitignore`
- Guarda tu contraseña de Supabase en un lugar seguro

## 🐛 **Troubleshooting**

### Error: "no such table"
- Verifica que las variables de entorno estén correctas en Vercel
- Asegúrate de que las migraciones se ejecutaron correctamente

### Error de conexión
- Verifica que la URL de conexión sea correcta
- Confirma que el proyecto de Supabase esté activo
- Revisa que la contraseña no tenga caracteres especiales sin escapar

### Logs de Vercel
- Ve a Functions → Revisa los logs para errores específicos
- Busca errores de conexión a la base de datos

¡Ya tienes todo configurado para usar Supabase! 🎉