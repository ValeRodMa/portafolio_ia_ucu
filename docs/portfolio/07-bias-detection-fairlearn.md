# Práctica 7: Detectar y Corregir Sesgo con Fairlearn

**UT2: Calidad & Ética | Práctica Interactiva - Dos Casos de Estudio**

## 🎯 Objetivos de Aprendizaje

- **DETECTAR** sesgo histórico en datasets reales (*Boston Housing* + *Titanic*)
- **ANALIZAR** impacto del sesgo en predicciones de modelos
- **COMPARAR** estrategias: detección (regresión) vs corrección (clasificación)
- **EVALUAR** cuándo detectar vs cuándo intentar corregir automáticamente
- **DESARROLLAR** criterios éticos para *deployment* responsable

## 📊 Metodología

### Parte I - Boston Housing: DETECTAR Sesgo Histórico
- Analizar sesgo oculto en variable **`B`** (proporción afroamericana)
- Cuantificar impacto del sesgo en predicciones (regresión)
- Analizar correlaciones y distribuciones por grupos raciales
- **No corregir** → enfoque en detección y análisis crítico

### Parte II - Titanic: DETECTAR + CORREGIR Sesgo Sistemático
- Detectar sesgo género/clase en protocolo *"Women and Children First"*
- Analizar interseccionalidad (género × clase social)
- Aplicar **Fairlearn** para corrección (clasificación natural)

### Parte III - Ames Housing: Aplicación Práctica
- Análisis de sesgo geográfico y socioeconómico
- Evaluación de variables proxy problemáticas

## 🔍 Resultados Principales

### Boston Housing Dataset
- **Brecha racial detectada**: -2.4% entre grupos de alta y baja proporción afroamericana
- **Correlación variable B**: 0.333 con precios de vivienda
- **Decisión ética**: Uso exclusivamente educativo, no para producción
- **Justificación**: Variable históricamente sesgada, inapropiada para modelos de producción

### Titanic Dataset
- **Brecha de género**: 54.8% diferencia en supervivencia (mujeres vs hombres)
- **Brecha de clase**: 41.3% diferencia entre primera y tercera clase
- **Aplicación Fairlearn**: 
  - Performance loss: 6.2%
  - Mejora en Demographic Parity: 0.051
- **Recomendación**: Evaluar caso por caso el trade-off precisión vs equidad

### Ames Housing Dataset
- **Brecha geográfica**: 45% entre barrios más y menos caros
- **Brecha temporal**: 28% diferencia entre casas nuevas vs antiguas
- **Riesgo**: Alto potencial de perpetuar desigualdades en contextos hipotecarios

## ⚖️ Framework Ético Desarrollado

### Cuándo **DETECTAR únicamente**
- Sesgo histórico complejo (Boston racial bias)
- Contexto de aprendizaje/investigación
- Variables proxy inevitables (neighborhood effects)

### Cuándo **DETECTAR + CORREGIR**
- Sesgo sistemático claro (Titanic gender bias)
- Contexto de producción con riesgo moderado
- Herramientas de fairness aplicables

### Cuándo **RECHAZAR el modelo**
- Alto impacto socioeconómico (lending, hiring)
- Sesgo severo no corregible
- Falta de transparencia en decisiones

## 🧠 Insights Técnicos

- **Detección vs Corrección**: Cada estrategia es apropiada para diferentes contextos
- **Sesgo histórico**: Más complejo de corregir que el sesgo sistemático
- **Context matters**: El dominio determina la tolerancia al sesgo
- **Fairlearn limitations**: No todas las situaciones de sesgo son corregibles automáticamente

## 🔧 Herramientas Utilizadas

- **Fairlearn**: Biblioteca principal para detección y corrección de sesgo
- **ExponentiatedGradient**: Algoritmo de corrección in-processing
- **DemographicParity**: Constraint de equidad demográfica
- **MetricFrame**: Análisis de métricas por grupos sensibles

## 💡 Reflexiones Éticas Críticas

### ¿Cuándo es más valioso *detectar* que *corregir automáticamente*?
Cuando el sesgo proviene de factores históricos profundos. La corrección automática puede ocultar la raíz del problema o generar resultados artificiales. La detección permite visibilizar y documentar el sesgo sin introducir ruido.

### ¿Cómo balancear *transparencia vs utilidad*?
La transparencia debe priorizarse frente a la utilidad. Un modelo con sesgo conocido y documentado es preferible a uno "ajustado" pero opaco, ya que los usuarios pueden comprender sus limitaciones.

### ¿Qué responsabilidades tenemos con *sesgos históricos no corregibles*?
Debemos identificarlos, explicarlos y advertir sobre sus implicancias. Si no se pueden eliminar, corresponde evitar su uso en contextos sensibles. La responsabilidad del data scientist es también social, no solo técnica.

## 🚀 Extensiones y Próximos Pasos

### Algoritmos Adicionales de Fairness
- **GridSearch**: Búsqueda exhaustiva de parámetros justos
- **ThresholdOptimizer**: Post-processing para optimizar umbrales
- **CorrelationRemover**: Pre-processing para eliminar correlaciones

### Constraints Alternativos
- **EqualizedOdds**: Igualdad de oportunidades
- **TruePositiveRateParity**: Paridad en True Positive Rate
- **FalsePositiveRateParity**: Paridad en False Positive Rate

## 📈 Impacto y Aplicaciones

Esta práctica demuestra la importancia crítica de:
- **Auditoría ética** en modelos de ML
- **Documentación transparente** de limitaciones
- **Evaluación contextual** de trade-offs
- **Responsabilidad social** en data science

El framework desarrollado es aplicable a cualquier dominio donde la equidad sea una consideración importante, especialmente en sectores como finanzas, recursos humanos, justicia y salud.

---

## 📁 Recursos

- **Notebook completo**: [Práctica7.ipynb](../assets/Práctica7.ipynb)
- **Fairlearn Documentation**: [fairlearn.org](https://fairlearn.org)
- **Datasets utilizados**: Boston Housing, Titanic, Ames Housing

---

*Esta práctica forma parte del curso de Ingeniería de Datos en IA, enfocándose en los aspectos éticos y de calidad en el desarrollo de modelos de machine learning.*
