# 🧹 Guía de Limpieza de Variables en Vercel

## 🚨 **Problema Detectado**
Tienes múltiples variables de base de datos que están causando conflictos:

### ❌ **Variables a ELIMINAR en Vercel:**
```
POSTGRES_URL
POSTGRES_PRISMA_URL  
SUPABASE_URL
NEXT_PUBLIC_SUPABASE_URL
POSTGRES_URL_NON_POOLING
SUPABASE_JWT_SECRET
POSTGRES_USER
NEXT_PUBLIC_SUPABASE_ANON_KEY
POSTGRES_PASSWORD
POSTGRES_DATABASE
SUPABASE_SERVICE_ROLE_KEY
POSTGRES_HOST
SUPABASE_ANON_KEY
```

### ✅ **Variables a MANTENER:**
```
DATABASE_URL = postgres://postgres.wcspwemadhshmqbfqsjn:HXdOX4PVMm7lMNad@db.wcspwemadhshmqbfqsjn.supabase.co:5432/postgres?sslmode=require
DJANGO_SETTINGS_MODULE = backend.settings
VERCEL = 1
```

## 🔧 **Pasos de Limpieza:**

### 1. **Acceder a Variables de Entorno**
- Ve a [vercel.com](https://vercel.com)
- Tu proyecto → **Settings** → **Environment Variables**

### 2. **Eliminar Variables Conflictivas**
Para cada variable en la lista "❌ Variables a ELIMINAR":
- Busca la variable
- Haz clic en los **3 puntos** (⋯) 
- Selecciona **Delete**
- Confirma la eliminación

### 3. **Verificar Variables Finales**
Al terminar debes tener SOLO estas 3 variables:
- ✅ `DATABASE_URL`
- ✅ `DJANGO_SETTINGS_MODULE`
- ✅ `VERCEL`

### 4. **Redeploy**
- Ve a **Deployments**
- Haz clic en **Redeploy** en el último deployment

## 🎯 **¿Por qué esto soluciona el problema?**

1. **Múltiples variables de DB** confunden a Django
2. **`POSTGRES_URL`** puede tener IPv6 que causa el error
3. **Variables automáticas** de Supabase son para Next.js, no Django
4. **Una sola variable** `DATABASE_URL` elimina ambigüedad

## 🧪 **Verificación Post-Limpieza**

Después de la limpieza y redeploy, tu API debe responder:
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

## 🔍 **Si sigue fallando:**

1. **Revisa los logs de Vercel** (Functions → Logs)
2. **Busca el mensaje debug** "Using DATABASE_URL: postgres://..."
3. **Verifica que solo aparezcan las 3 variables** en Environment Variables

¡Con esta limpieza tu API funcionará correctamente! 🎉