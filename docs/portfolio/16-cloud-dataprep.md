---
title: "Cloud Dataprep: preparación y transformación de datos sin código"
date: 2025-11-26
---

# Cloud Dataprep: preparación y transformación de datos sin código
{{ reading_time() }}

---
- **Autores**: Joaquín Batista, Milagros Cancela, Valentín Rodríguez, Alexia Aurrecoechea, Nahuel López (G1)
- **Unidad Temática**: UT5: Pipelines ETL
- **Tipo**: Práctica Guiada - Google Cloud Skills Boost Lab
- **Entorno**: Google Cloud Console + Cloud Dataprep (Trifacta)
- **Lab**: [Cloud Dataprep Lab](https://www.skills.google/focuses/4415?catalog_rank=%7B%22rank%22%3A6%2C%22num_filters%22%3A1%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=60910456)
- **Fecha**: Noviembre 2025

---

## 🎯 Objetivos de Aprendizaje

Cloud Dataprep es un servicio de Google Cloud que permite preparar y transformar datos de forma visual e interactiva sin necesidad de escribir código. Esta práctica explora cómo usar Cloud Dataprep para limpiar, transformar y enriquecer datos como parte de pipelines ETL, haciendo accesible la preparación de datos a usuarios no técnicos.

### Objetivos Principales

- **Comprender el concepto de preparación de datos** y su importancia en pipelines ETL
- **Explorar la interfaz visual de Cloud Dataprep** para transformaciones de datos
- **Aplicar transformaciones comunes** como limpieza, normalización, agregaciones y joins
- **Entender el flujo de trabajo** desde datos fuente hasta datos preparados listos para análisis
- **Apreciar las ventajas** de herramientas no-code/low-code para preparación de datos

---

## 📚 Lo que se Aprendió

### 1. **Preparación de Datos como Etapa Crítica del ETL**

**Concepto Fundamental:**
- La preparación de datos (data preparation) es una etapa esencial que consume típicamente 60-80% del tiempo en proyectos de ciencia de datos
- Involucra limpieza, transformación, normalización y enriquecimiento de datos crudos
- Datos mal preparados pueden llevar a análisis incorrectos y decisiones erróneas

**Desafíos Tradicionales:**
- Requiere conocimiento de programación (Python, SQL, etc.)
- Procesos manuales propensos a errores
- Difícil de documentar y reproducir
- Consume mucho tiempo en tareas repetitivas

**Solución con Cloud Dataprep:**
- Interfaz visual que elimina la necesidad de código
- Transformaciones sugeridas automáticamente basadas en patrones detectados
- Visualización inmediata de resultados antes de aplicar cambios
- Documentación automática del proceso de transformación

### 2. **Interfaz Visual y Flujo de Trabajo**

**Componentes Principales:**

**Flow (Flujo):**
- Representación visual del pipeline de transformación
- Cada paso es un "recipe" (receta) que define transformaciones
- Permite ver el flujo completo de datos desde fuentes hasta destino

**Recipe (Receta):**
- Conjunto de transformaciones aplicadas a un dataset
- Se puede editar paso a paso con visualización inmediata de resultados
- Permite deshacer/rehacer cambios fácilmente

**Sample (Muestra):**
- Cloud Dataprep trabaja con muestras de datos para mejorar rendimiento
- Las transformaciones se aplican primero a la muestra para validación
- Una vez validadas, se ejecutan sobre el dataset completo

**Transformaciones Visuales:**
- Selección de columnas mediante clics
- Filtros mediante menús desplegables
- Agregaciones mediante arrastrar y soltar
- Joins mediante conexión visual de datasets

### 3. **Tipos de Transformaciones Comunes**

**Limpieza de Datos:**
- Detección y eliminación de valores faltantes
- Corrección de tipos de datos incorrectos
- Normalización de formatos (fechas, números, texto)
- Eliminación de duplicados
- Manejo de outliers y valores anómalos

**Transformaciones de Columnas:**
- Renombrar columnas para claridad
- Dividir columnas en múltiples columnas (ej: nombre completo → nombre, apellido)
- Combinar columnas en una sola
- Crear columnas derivadas mediante fórmulas

**Agregaciones:**
- Agrupar por categorías
- Calcular sumas, promedios, conteos, máximos, mínimos
- Crear agregaciones condicionales

**Joins y Uniones:**
- Combinar datos de múltiples fuentes
- Diferentes tipos de joins (inner, left, right, full outer)
- Uniones basadas en claves comunes

**Enriquecimiento:**
- Agregar información geográfica (geocoding)
- Enriquecer con datos externos
- Crear features derivadas para machine learning

### 4. **Integración con Google Cloud**

**Fuentes de Datos:**
- Cloud Storage (GCS) - archivos CSV, JSON, Parquet, etc.
- BigQuery - tablas y vistas
- Cloud SQL - bases de datos relacionales
- Conectores a fuentes externas (APIs, bases de datos)

**Destinos de Datos:**
- BigQuery - para análisis y consultas SQL
- Cloud Storage - para almacenamiento de resultados
- Cloud SQL - para bases de datos relacionales

**Ejecución:**
- Cloud Dataprep ejecuta transformaciones usando Cloud Dataflow (Apache Beam)
- Escalado automático según el tamaño de los datos
- Ejecución programada mediante Cloud Scheduler
- Monitoreo de ejecuciones mediante Cloud Monitoring

### 5. **Detección Automática de Problemas**

**Data Quality Insights:**
- Cloud Dataprep analiza automáticamente los datos y detecta problemas comunes
- Sugiere transformaciones para resolver problemas detectados
- Proporciona estadísticas sobre calidad de datos (valores faltantes, duplicados, outliers)

**Ejemplos de Detecciones:**
- Columnas con muchos valores faltantes
- Inconsistencias en formatos de fecha
- Valores fuera de rango esperado
- Duplicados potenciales
- Tipos de datos incorrectos

---

## 🚧 Lo que Más Costó

### 1. **Comprensión del Modelo de Muestreo**

**Desafío:**
- Inicialmente fue confuso entender por qué Cloud Dataprep trabaja con muestras en lugar del dataset completo
- La diferencia entre ver resultados en la muestra vs. ejecutar sobre el dataset completo
- Entender cuándo los resultados de la muestra son representativos del dataset completo

**Solución Aprendida:**
- El muestreo permite iterar rápidamente sin procesar todo el dataset
- Es importante validar que las transformaciones funcionan correctamente en la muestra antes de ejecutar
- Para datasets grandes, el muestreo es esencial para mantener la interactividad de la herramienta
- Los resultados finales se ejecutan sobre el dataset completo cuando se programa la ejecución

### 2. **Construcción de Transformaciones Complejas**

**Desafío:**
- Aunque la interfaz es visual, construir transformaciones complejas requiere pensar en términos de pasos secuenciales
- Entender el orden correcto de las transformaciones (ej: limpiar antes de agregar)
- Manejar casos edge donde las transformaciones sugeridas automáticamente no son apropiadas

**Solución Aprendida:**
- Planificar el flujo de transformaciones antes de comenzar
- Aplicar transformaciones paso a paso y validar resultados intermedios
- Usar la funcionalidad de "preview" para ver resultados antes de confirmar cambios
- Documentar el propósito de cada transformación para referencia futura

### 3. **Manejo de Datos Heterogéneos**

**Desafío:**
- Cuando los datos provienen de múltiples fuentes con diferentes formatos y estructuras
- Unificar esquemas diferentes en un solo dataset
- Manejar inconsistencias en nombres de columnas, tipos de datos y formatos

**Solución Aprendida:**
- Normalizar datos de diferentes fuentes antes de combinarlos
- Usar transformaciones de tipo de datos para asegurar consistencia
- Crear columnas de mapeo para unificar nombres y valores diferentes
- Validar la integridad de los datos después de unir múltiples fuentes

### 4. **Optimización de Performance**

**Desafío:**
- Entender cómo las transformaciones afectan el tiempo de ejecución
- Optimizar el orden de las transformaciones para eficiencia
- Manejar datasets muy grandes que pueden tardar mucho en procesarse

**Solución Aprendida:**
- Filtrar datos temprano en el pipeline para reducir el volumen procesado
- Aplicar transformaciones más costosas después de reducir el tamaño del dataset
- Usar agregaciones para reducir la granularidad cuando sea apropiado
- Considerar particionar datos grandes en múltiples ejecuciones

### 5. **Integración con Otros Servicios**

**Desafío:**
- Configurar conexiones correctas a fuentes de datos (Cloud Storage, BigQuery)
- Entender permisos IAM necesarios para acceder a diferentes recursos
- Configurar destinos correctamente para que los datos transformados se guarden donde se necesitan

**Solución Aprendida:**
- Verificar permisos IAM antes de intentar acceder a recursos
- Usar service accounts con permisos mínimos necesarios
- Probar conexiones a fuentes de datos antes de construir transformaciones complejas
- Validar que los datos transformados se escriben correctamente en el destino

---

## ✨ Lo Nuevo que se Descubrió

### 1. **Preparación de Datos como Servicio Gestionado**

**Descubrimiento:**
- Cloud Dataprep está basado en la tecnología de Trifacta, una empresa líder en preparación de datos
- Es un servicio completamente gestionado, sin necesidad de configurar infraestructura
- Escala automáticamente según el tamaño de los datos procesados
- Se integra nativamente con otros servicios de Google Cloud

**Ventajas:**
- No hay que preocuparse por gestión de servidores o escalado manual
- Costos basados en uso real (solo pagas por lo que procesas)
- Actualizaciones y mejoras automáticas sin intervención del usuario
- Soporte y mantenimiento incluidos

### 2. **Sugerencias Inteligentes de Transformaciones**

**Descubrimiento:**
- Cloud Dataprep usa machine learning para sugerir transformaciones apropiadas
- Analiza patrones en los datos y propone soluciones comunes
- Aprende de transformaciones previas para mejorar sugerencias futuras

**Ejemplos:**
- Detecta automáticamente columnas de fecha y sugiere normalización de formato
- Identifica columnas categóricas y sugiere agrupaciones útiles
- Detecta valores faltantes y sugiere estrategias de imputación
- Sugiere joins cuando detecta relaciones potenciales entre datasets

### 3. **Visualización de Calidad de Datos en Tiempo Real**

**Descubrimiento:**
- Cloud Dataprep proporciona visualizaciones interactivas de la calidad de datos
- Muestra distribuciones, estadísticas y problemas de calidad mientras trabajas
- Permite identificar problemas de datos visualmente antes de aplicar transformaciones

**Beneficios:**
- Identificación rápida de outliers y anomalías
- Comprensión visual de distribuciones de datos
- Detección temprana de problemas de calidad
- Validación visual de que las transformaciones funcionan como se espera

### 4. **Colaboración y Versionado**

**Descubrimiento:**
- Cloud Dataprep permite colaboración en tiempo real entre múltiples usuarios
- Mantiene historial de cambios y permite comparar versiones de recipes
- Permite comentarios y anotaciones en transformaciones

**Aplicaciones:**
- Equipos pueden trabajar juntos en la preparación de datos
- Revisión de código (code review) para transformaciones de datos
- Documentación colaborativa del proceso de preparación
- Compartir conocimiento entre miembros del equipo

### 5. **Automatización y Programación**

**Descubrimiento:**
- Las transformaciones pueden ejecutarse de forma programada usando Cloud Scheduler
- Se pueden crear pipelines ETL completamente automatizados
- Integración con Cloud Composer (Apache Airflow) para orquestación compleja

**Casos de Uso:**
- Pipeline ETL diario que prepara datos frescos cada mañana
- Transformaciones que se ejecutan cuando llegan nuevos datos a Cloud Storage
- Preparación de datos como parte de un pipeline de ML más grande

---

## 💡 Algo Más Interesante

### 1. **Democratización de la Preparación de Datos**

Una de las características más interesantes de Cloud Dataprep es cómo democratiza la preparación de datos. Tradicionalmente, esta tarea requería:

- Conocimiento de programación (Python, R, SQL)
- Comprensión de estructuras de datos complejas
- Tiempo significativo para escribir y depurar código

Con Cloud Dataprep, usuarios de negocio, analistas y científicos de datos pueden preparar datos sin escribir una sola línea de código. Esto:

- **Reduce la barrera de entrada** para trabajar con datos
- **Acelera el tiempo de desarrollo** de pipelines ETL
- **Permite que expertos de dominio** (que conocen los datos pero no programan) participen activamente
- **Mejora la colaboración** entre equipos técnicos y no técnicos

### 2. **Preparación de Datos como Arte y Ciencia**

La preparación de datos es tanto un arte como una ciencia. Requiere:

**Aspectos Científicos:**
- Comprensión de estadísticas y distribuciones
- Conocimiento de técnicas de limpieza y transformación
- Entendimiento de estructuras de datos y algoritmos

**Aspectos Artísticos:**
- Intuición sobre qué transformaciones son apropiadas
- Creatividad para resolver problemas únicos de datos
- Juicio sobre cuándo los datos están "suficientemente limpios"

Cloud Dataprep facilita ambos aspectos: proporciona las herramientas científicas (transformaciones, estadísticas) mientras permite que el usuario aplique su intuición y creatividad de forma visual e interactiva.

### 3. **Impacto en la Velocidad de Desarrollo**

El impacto en la velocidad de desarrollo puede ser dramático:

**Enfoque Tradicional (con código):**
- Escribir código: 2-4 horas
- Depurar y probar: 1-2 horas
- Documentar: 30 minutos
- **Total: 3.5-6.5 horas**

**Con Cloud Dataprep:**
- Construir transformaciones visuales: 30-60 minutos
- Validar con preview: 15 minutos
- Documentar (automático): 0 minutos
- **Total: 45-75 minutos**

Esto representa una reducción del **80-90%** en tiempo de desarrollo, permitiendo iterar más rápido y experimentar con diferentes enfoques de preparación.

### 4. **Preparación de Datos como Base para ML**

La preparación de datos es especialmente crítica para machine learning:

- **Calidad de datos** directamente impacta la calidad del modelo
- **Features bien preparadas** pueden mejorar significativamente el rendimiento
- **Datos consistentes** son esenciales para entrenamiento y producción

Cloud Dataprep facilita la creación de features para ML:
- Transformaciones que crean features categóricas numéricas
- Normalización y escalado de features
- Creación de features derivadas (ej: edad a partir de fecha de nacimiento)
- Manejo de valores faltantes de forma apropiada para ML

### 5. **Evolución hacia DataOps**

Cloud Dataprep representa parte de una tendencia más amplia hacia DataOps:

**DataOps Principios:**
- Automatización de pipelines de datos
- Versionado y control de calidad
- Colaboración entre equipos
- Monitoreo y observabilidad
- Entrega continua de datos

Cloud Dataprep encaja perfectamente en este paradigma:
- Transformaciones versionadas y reproducibles
- Ejecución automatizada y programada
- Colaboración en tiempo real
- Integración con herramientas de CI/CD

Esto permite tratar los datos como código, con todos los beneficios que eso conlleva: testing, versionado, rollback, y deployment automatizado.

---

## 🎓 Reflexiones Finales

Cloud Dataprep demuestra cómo las herramientas visuales pueden hacer que tareas complejas sean accesibles sin sacrificar poder o flexibilidad. Para pipelines ETL, especialmente en entornos donde múltiples personas necesitan preparar datos, Cloud Dataprep ofrece una solución elegante que combina facilidad de uso con capacidades avanzadas.

**Ventajas Clave:**
- **Accesibilidad**: No requiere conocimiento de programación
- **Velocidad**: Desarrollo mucho más rápido que código tradicional
- **Colaboración**: Múltiples usuarios pueden trabajar juntos
- **Integración**: Se integra perfectamente con el ecosistema de Google Cloud
- **Escalabilidad**: Maneja datasets de cualquier tamaño automáticamente

**Cuándo Usar Cloud Dataprep:**
- Preparación de datos exploratoria y ad-hoc
- Cuando usuarios no técnicos necesitan preparar datos
- Para documentar y compartir procesos de preparación
- Como parte de pipelines ETL automatizados
- Para enriquecer datos con transformaciones visuales

**Cuándo Considerar Alternativas:**
- Transformaciones extremadamente complejas que requieren lógica personalizada
- Cuando ya existe código de preparación bien establecido
- Para transformaciones que requieren bibliotecas específicas no disponibles

---

## 📚 Recursos Adicionales

- [Cloud Dataprep Documentation](https://cloud.google.com/dataprep/docs)
- [Trifacta Wrangler (versión desktop)](https://www.trifacta.com/)
- [Google Cloud Skills Boost - Data Engineering Path](https://www.cloudskillsboost.google/paths)
- [Best Practices for Data Preparation](https://cloud.google.com/dataprep/docs/best-practices)

---

> 💡 **Nota**: Cloud Dataprep es especialmente valioso en equipos multidisciplinarios donde tanto analistas de negocio como ingenieros de datos necesitan preparar datos. Su interfaz visual y sugerencias inteligentes aceleran significativamente el desarrollo de pipelines ETL.

