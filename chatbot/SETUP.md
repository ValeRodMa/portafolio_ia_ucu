# 🚀 Guía de Setup del Chatbot

## Paso 1: Instalar dependencias

```bash
# Desde la raíz del proyecto
pip install -r chatbot/requirements.txt
```

O instalar manualmente:
```bash
pip install openai python-dotenv flask flask-cors numpy tiktoken
```

## Paso 2: Configurar API Key de OpenAI

1. Obtén tu API key de OpenAI: https://platform.openai.com/api-keys
2. Crea archivo `.env` en la raíz del proyecto:
```bash
echo "OPENAI_API_KEY=sk-tu-api-key-aqui" >> .env
```

**⚠️ IMPORTANTE:** El archivo `.env` está en `.gitignore` y NO se subirá al repositorio.

## Paso 3: Extraer contenido del portfolio

```bash
python chatbot/scripts/extract_content.py
```

Esto creará `chatbot/data/content_chunks.json` con todo el contenido del portfolio dividido en chunks.

## Paso 4: Generar embeddings

```bash
python chatbot/scripts/generate_embeddings.py
```

Esto generará `chatbot/embeddings/embeddings.json` con los embeddings de OpenAI.

**💰 Costo:** Aproximadamente $0.01-0.05 USD por ejecución (depende del tamaño del portfolio).

## Paso 5: Iniciar servidor backend

```bash
python chatbot/backend/app.py
```

El servidor estará disponible en `http://localhost:5000`

## Paso 6: Probar el chatbot

1. Inicia el servidor de MkDocs:
```bash
mkdocs serve
```

2. Abre el portfolio en el navegador
3. Verás un botón flotante 💬 en la esquina inferior derecha
4. Haz clic y prueba hacer una pregunta sobre el portfolio

## 🔧 Solución de problemas

### Error: "OPENAI_API_KEY no encontrada"
- Verifica que el archivo `.env` esté en la raíz del proyecto
- Verifica que tenga el formato correcto: `OPENAI_API_KEY=sk-...`

### Error: "No se encontró embeddings.json"
- Ejecuta primero `generate_embeddings.py`

### El chatbot no aparece en el sitio
- Verifica que `chatbot.js` esté en `docs/assets/javascripts/`
- Verifica que esté agregado en `mkdocs.yml` en `extra_javascript`
- Recarga la página con Ctrl+F5

### El chatbot no responde
- Verifica que el servidor backend esté corriendo en `http://localhost:5000`
- Abre la consola del navegador (F12) para ver errores
- Verifica que la API key sea válida

## 📝 Notas

- El chatbot solo funciona localmente por ahora (backend en localhost:5000)
- Para producción, necesitarías desplegar el backend en un servicio como Render, Railway, o Vercel
- Los embeddings se generan una vez y se reutilizan (no necesitas regenerarlos a menos que cambies el contenido)

