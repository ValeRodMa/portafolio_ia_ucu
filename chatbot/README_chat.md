# Chatbot con IA para el Portfolio

Chatbot inteligente que responde preguntas sobre el contenido del portfolio usando RAG (Retrieval Augmented Generation) con OpenAI. 
El sistema busca información relevante en el portfolio y la usa como contexto para que GPT-3.5-turbo responda de manera precisa y contextualizada.

----------
## Arquitectura
```
chatbot/
├── backend/           # API Flask que procesa preguntas y genera respuestas
├── frontend/          # Widget JavaScript que se integra con MkDocs
├── data/              # Contenido extraído del portfolio (chunks de texto)
├── embeddings/        # Embeddings generados con OpenAI (vectores numéricos)
└── scripts/          # Scripts para extraer contenido y generar embeddings
```
----------
## ¿Cómo Funciona?

El chatbot funciona en 3 etapas principales:

1. **Extracción de contenido**: Se leen todos los archivos markdown del portfolio, se limpia la sintaxis markdown y se dividen en pedacitos pequeños (chunks) para facilitar la búsqueda.

2. **Generación de embeddings**: Cada chunk de texto se convierte en un vector numérico usando la API de embeddings de OpenAI (`text-embedding-3-small`). Estos vectores representan el significado semántico del texto y se guardan en un JSON para reutilizarlos.

3. **Búsqueda y respuesta**: Cuando un usuario hace una pregunta:
   - Se genera un embedding de la pregunta
   - Se busca similitud con todos los embeddings guardados
   - Se recuperan los 3 chunks más relevantes (optimizado para velocidad)
   - Esos chunks se envían como contexto a GPT-3.5-turbo junto con la pregunta
   - GPT genera una respuesta basada únicamente en el contexto del portfolio

----------
## Componentes Detallados

### `scripts/calculate_metrics.py`
**Qué hace**: Analiza todos los archivos markdown del portfolio y calcula métricas y estadísticas.

**Métricas calculadas**:
- Total de entradas, palabras, imágenes, bloques de código
- Entrada más larga, con más gráficas, con más código
- Datasets y tecnologías utilizadas
- Rankings y comparativas

**Genera**:
- `data/portfolio_metrics.json`: Datos estructurados en JSON
- `data/portfolio_metrics.md`: Documento legible con todas las estadísticas

**Por qué es necesario**: Permite que el chatbot responda preguntas sobre métricas del portfolio (ej: "¿cuál es la entrada más larga?", "¿cuántas gráficas hay?").

### `scripts/extract_content.py`
**Qué hace**: Extrae todo el contenido de los archivos markdown del portfolio y lo prepara para generar embeddings.

**Proceso**:
- Recorre recursivamente la carpeta `docs/` buscando archivos `.md`
- Incluye automáticamente el documento de métricas si existe
- Limpia la sintaxis markdown (remueve código, imágenes, headers, etc.)
- Divide el contenido en chunks de tamaño manejable
- Extrae metadata (título, URL, ruta del archivo)
- Guarda todo en `data/content_chunks.json`

**Por qué es necesario**: Necesitamos el contenido en formato texto plano y dividido en pedacitos para poder generar embeddings y buscar información relevante después.

### `backend/app.py`
**Qué hace**: API Flask que recibe preguntas del frontend, busca información relevante y genera respuestas usando GPT-3.5-turbo.

**Endpoints**:
- `GET /health`: Verifica que el servidor esté funcionando y los embeddings estén cargados
- `POST /chat`: Recibe una pregunta, busca chunks relevantes y genera una respuesta

----------
## ¿Cómo se usa?

Una vez configurado, el chatbot se integra automáticamente en MkDocs. 
Los usuarios pueden:
- Hacer clic en el botón flotante 💬
- Escribir preguntas sobre el contenido del portfolio
- Ver respuestas contextualizadas con referencias a las fuentes
- Navegar directamente a las prácticas mencionadas

### Preguntas de ejemplo para probar:

**Sobre contenido de prácticas:**
- "¿Qué es la práctica 11?"
- "Explícame sobre feature engineering temporal"
- "Háblame sobre Google Cloud Dataprep"
- "¿Cuáles son las técnicas de análisis de datos que has usado?"

**Sobre métricas del portfolio:**
- "¿Cuál es la entrada más larga del portfolio?"
- "¿Cuántas gráficas se generaron en total?"
- "¿Qué práctica tiene más visualizaciones?"
- "¿Cuántas prácticas hay en total?"
- "¿Qué datasets usaste en el portfolio?"
- "¿Qué tecnologías y librerías se utilizaron?"

### Optimizaciones recientes:
- **Velocidad mejorada**: Reducido de 5 a 3 chunks por consulta (30-40% más rápido)
- **Respuestas más concisas**: Máximo 350 tokens (antes 500)
- **Solo contenido del portfolio**: El chatbot rechaza preguntas no relacionadas con el portfolio
- **Umbral de similitud**: Solo responde si hay suficiente relevancia (≥0.4)
- **Temperatura reducida**: Respuestas más consistentes y predecibles (0.3 vs 0.7)

----------
## Actualizar Métricas y Contenido

Cuando agregues o modifiques contenido del portfolio, necesitas actualizar las métricas y regenerar los embeddings.

### Opción 1: Script completo (recomendado)
```bash
python3 chatbot/scripts/update_all.py
```

Este script ejecuta automáticamente:
1. Cálculo de métricas del portfolio
2. Extracción de contenido (incluye métricas)
3. Generación de embeddings

### Opción 2: Paso a paso
```bash
# 1. Calcular métricas
python3 chatbot/scripts/calculate_metrics.py

# 2. Extraer contenido
python3 chatbot/scripts/extract_content.py

# 3. Generar embeddings
python3 chatbot/scripts/generate_embeddings.py
```

**Nota**: El proceso completo toma ~2-3 minutos y cuesta aproximadamente $0.005 USD en llamadas a OpenAI API.

Para más detalles sobre las métricas, consulta [METRICS_README.md](./METRICS_README.md).

----------
## Despliegue en Producción

El chatbot está desplegado en **Render**:
- **Backend**: https://portafolio-ia-ucu.onrender.com
- **Frontend**: Se integra automáticamente en GitHub Pages
- **Plan**: Verificar en [Render Dashboard](https://dashboard.render.com/) → Instance Type
  - Free: Con sleep después de 15 min de inactividad
  - Starter ($7/mes): Sin sleep, siempre activo


----------
## Costos Estimados
- **Render Starter** (sin sleep): $7/mes
- **OpenAI API** (uso moderado, ~1000 preguntas/mes): $5-10 USD
- **Total mensual estimado**: $12-17 USD

_Nota: Si usas el plan Free de Render, el costo es $0 pero el servicio "duerme" después de 15 minutos de inactividad._