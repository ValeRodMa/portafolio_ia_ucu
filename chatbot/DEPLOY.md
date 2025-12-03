# 🚀 Guía de Despliegue del Backend del Chatbot

Esta guía te ayudará a desplegar el backend del chatbot en **Render** (gratis y fácil).

## 📋 Requisitos Previos

1. Cuenta en GitHub (ya la tienes)
2. Cuenta en Render (gratuita): https://render.com
3. API Key de OpenAI (ya la tienes)

## 🎯 Paso 1: Preparar el Repositorio

Los archivos necesarios ya están creados:
- ✅ `chatbot/Procfile` - Configuración para Render
- ✅ `chatbot/backend/wsgi.py` - Punto de entrada WSGI
- ✅ `chatbot/requirements.txt` - Dependencias (incluye gunicorn)

## 🎯 Paso 2: Crear Cuenta en Render

1. Ve a https://render.com
2. Haz clic en "Get Started for Free"
3. Conecta tu cuenta de GitHub
4. Autoriza a Render a acceder a tus repositorios

## 🎯 Paso 3: Crear un Nuevo Web Service

1. En el dashboard de Render, haz clic en **"New +"** → **"Web Service"**
2. Conecta tu repositorio `portafolio_ia_ucu`
3. Configura el servicio:
   - **Name**: `portfolio-chatbot-backend` (o el nombre que prefieras)
   - **Region**: Elige la más cercana (ej: `Oregon (US West)`)
   - **Branch**: `main`
   - **Root Directory**: `chatbot` ⚠️ **IMPORTANTE**: Debe ser `chatbot`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --chdir backend wsgi:app --bind 0.0.0.0:$PORT`

## 🎯 Paso 4: Configurar Variables de Entorno

En la sección **"Environment Variables"** de Render, agrega:

- **Key**: `OPENAI_API_KEY`
- **Value**: Tu API key de OpenAI (empieza con `sk-...`)

⚠️ **IMPORTANTE**: No compartas tu API key públicamente.

## 🎯 Paso 5: Subir los Embeddings

El backend necesita el archivo `embeddings.json`. Tienes dos opciones:

### Opción A: Subir el archivo al repositorio (Recomendado)

1. Asegúrate de que `chatbot/embeddings/embeddings.json` existe localmente
2. Si está en `.gitignore`, remuévelo temporalmente:
   ```bash
   git add -f chatbot/embeddings/embeddings.json
   git commit -m "Add embeddings for deployment"
   git push
   ```

### Opción B: Regenerar en Render (Más complejo)

Puedes crear un script de build que genere los embeddings, pero es más complicado.

## 🎯 Paso 6: Desplegar

1. Haz clic en **"Create Web Service"**
2. Render comenzará a construir y desplegar tu servicio
3. Espera 2-5 minutos mientras se instalan las dependencias
4. Una vez completado, verás una URL como: `https://portfolio-chatbot-backend.onrender.com`

## 🎯 Paso 7: Probar el Backend

1. Visita: `https://tu-url.onrender.com/health`
2. Deberías ver: `{"status": "ok", "embeddings_loaded": true}`

## 🎯 Paso 8: Actualizar el Frontend

Una vez que tengas la URL de tu backend, actualiza `docs/assets/javascripts/chatbot.js`:

```javascript
const API_URL = isProduction 
    ? 'https://tu-url.onrender.com/chat'  // ← Cambia esto por tu URL real
    : 'http://localhost:5000/chat';
```

Luego haz commit y push:
```bash
git add docs/assets/javascripts/chatbot.js
git commit -m "Update chatbot API URL for production"
git push
```

## 🔧 Solución de Problemas

### Error: "embeddings_loaded": false
- Verifica que `embeddings.json` esté en el repositorio
- Verifica que la ruta en `app.py` sea correcta

### Error: "OPENAI_API_KEY no encontrada"
- Verifica que la variable de entorno esté configurada en Render
- Asegúrate de que el nombre sea exactamente `OPENAI_API_KEY`

### El servicio se duerme después de inactividad
- Render tiene un plan gratuito que "duerme" servicios después de 15 minutos de inactividad
- La primera petición después de dormir puede tardar ~30 segundos
- Para evitar esto, puedes usar un servicio de "ping" o actualizar a un plan de pago

### CORS Error
- El código ya incluye `CORS(app)` que debería solucionarlo
- Si persiste, verifica que el frontend esté usando la URL correcta

## 💰 Costos

- **Render**: Gratis (con limitaciones de "sleep" después de inactividad)
- **OpenAI API**: ~$5-15 USD/mes (depende del uso)

## 📝 Notas Adicionales

- El servicio gratuito de Render puede tardar ~30 segundos en "despertar" si ha estado inactivo
- Para producción seria, considera actualizar a un plan de pago
- Alternativamente, puedes usar Railway, Vercel, o cualquier otro servicio que soporte Flask

