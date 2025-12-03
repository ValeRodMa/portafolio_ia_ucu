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
## ¿Cómo Funciona?X

El chatbot funciona en 3 etapas principales:

1. **Extracción de contenido**: Se leen todos los archivos markdown del portfolio, se limpia la sintaxis markdown y se dividen en pedacitos pequeños (chunks) para facilitar la búsqueda.

2. **Generación de embeddings**: Cada chunk de texto se convierte en un vector numérico usando la API de embeddings de OpenAI (`text-embedding-3-small`). Estos vectores representan el significado semántico del texto y se guardan en un JSON para reutilizarlos.

3. **Búsqueda y respuesta**: Cuando un usuario hace una pregunta:
   - Se genera un embedding de la pregunta
   - Se busca similitud con todos los embeddings guardados
   - Se recuperan los 5 chunks más relevantes
   - Esos chunks se envían como contexto a GPT-3.5-turbo junto con la pregunta
   - GPT genera una respuesta basada únicamente en el contexto del portfolio

----------
## Componentes Detallados

### `scripts/extract_content.py`
**Qué hace**: Extrae todo el contenido de los archivos markdown del portfolio y lo prepara para generar embeddings.

**Proceso**:
- Recorre recursivamente la carpeta `docs/` buscando archivos `.md`
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

----------
## Costos Estimados
- **Estimación mensual** (uso moderado, ~1000 preguntas): $5-15 USD