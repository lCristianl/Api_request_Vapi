# 🔧 Solución para Problema de Conectividad IPv6

## 🚨 **Problema**
```
connection to server at "db.wcspwemadhshmqbfqsjn.supabase.co" (2600:1f18:2e13:9d23:69a:653a:7277:c3ce), port 5432 failed: Cannot assign requested address
```

**Causa:** Vercel no puede conectarse via IPv6 al servidor directo de Supabase.

## 🛠️ **Soluciones a Probar (en orden)**

### **Opción 1: Pooler de Supabase (Recomendado)**
```
postgres://postgres.wcspwemadhshmqbfqsjn:HXdOX4PVMm7lMNad@aws-0-us-east-1.pooler.supabase.com:5432/postgres?sslmode=require
```

### **Opción 2: Pooler alternativo**
```
postgres://postgres.wcspwemadhshmqbfqsjn:HXdOX4PVMm7lMNad@aws-1-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require
```

### **Opción 3: Variables separadas**
Si las URLs no funcionan, usa variables separadas:
```
DB_HOST = aws-0-us-east-1.pooler.supabase.com
DB_NAME = postgres
DB_USER = postgres.wcspwemadhshmqbfqsjn
DB_PASSWORD = HXdOX4PVMm7lMNad
DB_PORT = 5432
```

## 🎯 **Pasos de Implementación**

### **Paso 1: Probar Opción 1**
1. Ve a **Vercel** → Settings → Environment Variables
2. Edita `DATABASE_URL` con la **Opción 1**
3. **Redeploy** y prueba

### **Paso 2: Si falla, probar Opción 2**
1. Cambia `DATABASE_URL` a la **Opción 2**
2. **Redeploy** y prueba

### **Paso 3: Si ambas fallan, usar variables separadas**
1. **Elimina** `DATABASE_URL`
2. **Agrega** las variables de la **Opción 3**
3. **Redeploy** y prueba

## 🔍 **Cómo verificar que funciona**

### **En los logs de Vercel:**
- Busca: `"Using DATABASE_URL: postgres://..."`
- O: `"Using manual DB configuration"`

### **En la respuesta de tu API:**
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

## 💡 **¿Por qué funciona el pooler?**

1. **El pooler maneja IPv4/IPv6** automáticamente
2. **Optimizado para conexiones externas** como Vercel
3. **Mejor manejo de timeouts** y reconexiones
4. **Específicamente diseñado** para aplicaciones serverless

## 🚨 **Si nada funciona**

**Última opción:** Usar **PlanetScale** o **Railway** como alternativa a Supabase para PostgreSQL.

¡Prueba las opciones en orden y una debería funcionar! 🎉