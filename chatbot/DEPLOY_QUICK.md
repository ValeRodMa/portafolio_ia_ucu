# 🚀 Despliegue Rápido del Chatbot en Render

## ⚡ Pasos Rápidos

### 1. Preparar embeddings para producción

El archivo `embeddings.json` está en `.gitignore` pero lo necesitamos para producción. Tienes dos opciones:

**Opción A: Agregar al repositorio (Recomendado - más simple)**
```bash
# Remover temporalmente del .gitignore
git add -f chatbot/embeddings/embeddings.json
git commit -m "Add embeddings for production deployment"
git push
```

**Opción B: Regenerar en Render (Más complejo)**
- Necesitarías crear un script de build que genere los embeddings
- Requiere configurar la API key antes del build

### 2. Crear cuenta en Render

1. Ve a https://render.com
2. Regístrate con GitHub (gratis)
3. Conecta tu repositorio `portafolio_ia_ucu`

### 3. Crear Web Service

1. Click en **"New +"** → **"Web Service"**
2. Selecciona tu repositorio
3. Configuración:
   - **Name**: `portfolio-chatbot-backend`
   - **Root Directory**: `chatbot` ⚠️ IMPORTANTE
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --chdir backend wsgi:app --bind 0.0.0.0:$PORT`

### 4. Variables de Entorno

En **Environment Variables**, agrega:
- `OPENAI_API_KEY` = `sk-tu-api-key-aqui`

### 5. Desplegar

Click en **"Create Web Service"** y espera 2-5 minutos.

### 6. Obtener URL

Una vez desplegado, copia la URL (ej: `https://portfolio-chatbot-backend.onrender.com`)

### 7. Actualizar Frontend

Edita `docs/assets/javascripts/chatbot.js` línea 14:
```javascript
const API_URL = isProduction 
    ? 'https://TU-URL-AQUI.onrender.com/chat'  // ← Pega tu URL aquí
    : 'http://localhost:5000/chat';
```

Luego:
```bash
git add docs/assets/javascripts/chatbot.js
git commit -m "Update chatbot API URL"
git push
```

### 8. Probar

1. Visita `https://TU-URL.onrender.com/health`
2. Deberías ver: `{"status": "ok", "embeddings_loaded": true}`
3. Visita tu portfolio y prueba el chatbot 💬

## ⚠️ Notas Importantes

- El servicio gratuito de Render "duerme" después de 15 min de inactividad
- La primera petición después de dormir puede tardar ~30 segundos
- Para evitar esto, considera un plan de pago o un servicio de "ping"

## 📖 Guía Completa

Para más detalles, ver `DEPLOY.md`

