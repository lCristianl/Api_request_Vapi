# 🚀 Configuración de Variables de Entorno en Vercel

## ⚡ Variables Exactas para tu Proyecto

Ve a tu proyecto en Vercel → **Settings** → **Environment Variables** y agrega estas variables:

### 📋 **Variables Requeridas:**

```bash
# Configuración de Base de Datos (URL CORREGIDA)
DATABASE_URL = postgres://postgres.wcspwemadhshmqbfqsjn:HXdOX4PVMm7lMNad@db.wcspwemadhshmqbfqsjn.supabase.co:5432/postgres?sslmode=require

# Configuración de Django
DJANGO_SETTINGS_MODULE = backend.settings

# Indicador de producción
VERCEL = 1
```

### 🎯 **Pasos en Vercel:**

1. Ve a [vercel.com](https://vercel.com) → Tu proyecto
2. **Settings** → **Environment Variables**
3. **Add New** para cada variable:

   **Variable 1:**
   - Name: `DATABASE_URL`
   - Value: `postgres://postgres.wcspwemadhshmqbfqsjn:HXdOX4PVMm7lMNad@db.wcspwemadhshmqbfqsjn.supabase.co:5432/postgres?sslmode=require`
   - Environment: All (Production, Preview, Development)

   **Variable 2:**
   - Name: `DJANGO_SETTINGS_MODULE`
   - Value: `backend.settings`
   - Environment: All

   **Variable 3:**
   - Name: `VERCEL`
   - Value: `1`
   - Environment: All

4. **Save** cada variable

### 🔄 **Después de configurar:**

1. Ve a la pestaña **Deployments**
2. Haz clic en **Redeploy** en el último deployment
3. O simplemente haz un commit para triggerar un nuevo deployment:

```bash
git add .
git commit -m "Configure Supabase database connection"
git push origin main
```

## 🧪 **Probar la API**

Una vez redesplegado, prueba tu endpoint:

**URL:** `https://tu-proyecto.vercel.app/api/usuarios/`

**Método:** POST

**Body:**
```json
{
    "cedula": "1150334017"
}
```

**Response esperada:**
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

## 🔍 **Verificar en Supabase**

1. Ve a tu proyecto en Supabase
2. **Table Editor**
3. Deberías ver la tabla `api_request_usuario` con tu usuario de prueba

## ⚠️ **Si hay errores:**

1. **Revisa los logs de Vercel:**
   - Functions → Logs
   - Busca errores de conexión

2. **Errores comunes:**
   - "no such table" → Las migraciones no se ejecutaron
   - "connection refused" → Variables de entorno incorrectas
   - "authentication failed" → Contraseña incorrecta

## 💡 **Notas importantes:**

- La base de datos se configurará automáticamente en el primer despliegue
- El usuario de prueba se creará automáticamente
- No necesitas ejecutar migraciones manualmente en Vercel
- Supabase manejará todas las conexiones SSL automáticamente

¡Ya estás listo para usar tu API con Supabase! 🎉