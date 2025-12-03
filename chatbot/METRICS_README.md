# Sistema de Métricas del Portfolio

El chatbot ahora puede responder preguntas sobre métricas y estadísticas del portfolio.

## ¿Qué métricas están disponibles?

El sistema calcula automáticamente:

- **Métricas generales**:
  - Total de entradas/prácticas
  - Total de palabras
  - Total de imágenes/gráficas
  - Total de bloques de código
  - Promedios por entrada

- **Récords y destacados**:
  - Entrada más larga (por contenido)
  - Entrada con más gráficas/imágenes
  - Entrada con más código

- **Recursos utilizados**:
  - Datasets utilizados
  - Tecnologías y librerías
  - Distribución por categorías

- **Métricas por entrada**:
  - Palabras por entrada
  - Gráficas por entrada
  - Código por entrada
  - Datasets utilizados en cada entrada

## Ejemplos de preguntas que el chatbot puede responder

### Preguntas sobre récords
- "¿Cuál es la entrada más larga del portfolio?"
- "¿Qué práctica tiene más gráficas?"
- "¿Cuál es el proyecto con más código?"

### Preguntas sobre totales
- "¿Cuántas prácticas hay en total?"
- "¿Cuántas gráficas se generaron en el portfolio?"
- "¿Cuántos bloques de código hay?"

### Preguntas sobre recursos
- "¿Qué datasets se utilizaron?"
- "¿Qué tecnologías o librerías se usaron?"
- "¿En cuántas prácticas se usó pandas?"

### Preguntas comparativas
- "¿Cuáles son las 5 entradas más largas?"
- "¿Qué entradas tienen más visualizaciones?"

## Cómo actualizar las métricas

Cuando agregues o modifiques contenido del portfolio:

### Opción 1: Script completo (recomendado)
```bash
python3 chatbot/scripts/update_all.py
```

Este script ejecuta automáticamente:
1. Cálculo de métricas
2. Extracción de contenido
3. Generación de embeddings

### Opción 2: Paso a paso
```bash
# 1. Calcular métricas
python3 chatbot/scripts/calculate_metrics.py

# 2. Extraer contenido (incluye métricas)
python3 chatbot/scripts/extract_content.py

# 3. Generar embeddings
python3 chatbot/scripts/generate_embeddings.py
```

## Archivos generados

El sistema genera los siguientes archivos:

- `chatbot/data/portfolio_metrics.json` - Datos JSON con todas las métricas
- `chatbot/data/portfolio_metrics.md` - Documento markdown legible con las métricas
- `chatbot/data/content_chunks.json` - Chunks de contenido incluyendo métricas
- `chatbot/embeddings/embeddings.json` - Embeddings para búsqueda semántica

## Arquitectura

```
Portfolio (.md files)
    ↓
calculate_metrics.py → portfolio_metrics.md/json
    ↓
extract_content.py → content_chunks.json (incluye métricas)
    ↓
generate_embeddings.py → embeddings.json
    ↓
Chatbot puede responder sobre métricas
```

## Métricas calculadas automáticamente

### Por archivo
- Conteo de palabras (excluyendo código)
- Conteo de caracteres
- Número de líneas
- Número de imágenes/gráficas
- Número de bloques de código
- Número de fragmentos de código inline
- Datasets mencionados
- Tecnologías mencionadas

### Agregadas
- Totales de todas las métricas
- Promedios
- Rankings (top 5 por categoría)
- Distribución por secciones

## Notas técnicas

- Las métricas se calculan analizando la sintaxis markdown
- Se excluye el código de los conteos de palabras
- Los datasets y tecnologías se detectan por palabras clave comunes
- El documento de métricas se incluye automáticamente en los embeddings

## Mantenimiento

Las métricas se deben actualizar:
- Después de agregar nuevas prácticas
- Después de modificar contenido existente
- Antes de desplegar cambios al chatbot en producción

El proceso completo toma aproximadamente 2-3 minutos y cuesta ~$0.005 USD en llamadas a la API de OpenAI.

