# Missing Data Detective: análisis forense del dataset California Housing
{{ reading_time() }}
---
- **Autor**: Valentín Rodríguez
- **Fecha**: Octubre 2025
- **Unidad Temática**: UT2: Calidad & Ética (Dataset Alternativo)
- **Entorno**: Python + Pandas + Scikit-learn + Matplotlib + Seaborn
- **Dataset**: California Housing Dataset (20,640 muestras, 8 variables)

---

## 📋 Descripción General

Esta práctica representa una **versión alternativa** del análisis de datos faltantes y outliers, utilizando el **California Housing Dataset** en lugar del tradicional Ames Housing. El objetivo es demostrar versatilidad en el análisis de calidad de datos aplicando las mismas metodologías a diferentes dominios inmobiliarios.

### 🔍 Nota sobre Elección Ética del Dataset

**¿Por qué California Housing y no Boston Housing?**

El dataset de Boston Housing fue removido de `scikit-learn` desde la versión 1.2 debido a **problemas éticos documentados**:

- Los autores originales crearon una variable "B" asumiendo que la auto-segregación racial tenía un impacto positivo en los precios de viviendas
- El objetivo de la investigación original era estudiar calidad del aire, pero no demostró adecuadamente la validez de sus asunciones
- Los mantenedores de scikit-learn desaconsejan fuertemente su uso, excepto para educar sobre problemas éticos en ciencia de datos

**Alternativa elegida:** California Housing Dataset (1990) proporciona un contexto similar (mercado inmobiliario estadounidense) sin las implicaciones éticas problemáticas, permitiendo un análisis riguroso y responsable de datos faltantes.

## 🎯 Objetivos Principales

- **Detectar patrones** de missing data (MCAR, MAR, MNAR) en datos inmobiliarios
- **Identificar outliers** usando métodos estadísticos robustos
- **Implementar estrategias** de imputación apropiadas para el dominio
- **Crear pipelines** de limpieza reproducibles y anti-leakage
- **Considerar aspectos éticos** en el tratamiento de datos socioeconómicos

## 🔧 Tecnologías y Herramientas

- **Python** con bibliotecas especializadas:
  - `pandas` y `numpy`: Manipulación y análisis de datos
  - `scikit-learn`: Imputación, pipelines y anti-leakage
  - `matplotlib` y `seaborn`: Visualización avanzada
  - `scipy`: Análisis estadístico de outliers

## 📊 Dataset y Metodología

**Dataset:** California Housing Dataset (Scikit-learn)

- **Dimensiones:** 20,640 muestras × 8 variables
- **Variables inmobiliarias:** 8 atributos del mercado californiano (1990)
- **Variable objetivo:** MEDV (precio mediano de viviendas en unidades de $100,000)
- **Fuente:** [Scikit-learn Datasets](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)

**Acceso al notebook completo:** [Práctica 5B - California Housing Missing Data](Practica_05b_California_Housing_Missing_Data.ipynb)

### Variables Principales Analizadas

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `MedInc` | Numérica | Ingreso mediano del grupo de bloques (unidades de $10,000) |
| `HouseAge` | Numérica | Edad mediana de las casas en el grupo de bloques |
| `AveRooms` | Numérica | Número promedio de habitaciones por hogar |
| `AveBedrms` | Numérica | Número promedio de dormitorios por hogar |
| `Population` | Numérica | Población del grupo de bloques |
| `AveOccup` | Numérica | Número promedio de miembros del hogar |
| `Latitude` | Numérica | Latitud del grupo de bloques |
| `Longitude` | Numérica | Longitud del grupo de bloques |
| `MEDV` | Target | Valor mediano de viviendas (unidades de $100,000) |

## 🔍 Análisis de Missing Data

### Patrones de Missing Data Sintéticos

![Patrones de Missing Data](../assets/california-housing-missing-patterns.png)
*Análisis de patrones de datos faltantes en el dataset California Housing*

**Tipos identificados:**

- **MCAR (AveOccup)**: Missing completamente al azar - 8% de valores faltantes
- **MAR (AveRooms)**: Missing relacionado con HouseAge - edificios antiguos tienen más missing
- **MNAR (MEDV)**: Missing relacionado con precio alto - propiedades caras no reportan valor

### Clasificación MCAR/MAR/MNAR

**Análisis por patrones:**

- **NOX**: Distribución aleatoria sin correlación con variables observables
- **RM**: Concentración en edificios construidos antes de 1940 (AGE > percentil 70)
- **MEDV**: Valores faltantes en propiedades con precio > percentil 85

## 📊 Detección de Outliers

![Análisis de Outliers](../assets/california-housing-outliers-analysis.png)
*Detección de outliers usando métodos IQR y Z-Score*

### Métodos Aplicados

- **IQR (Interquartile Range)**: Robusto para distribuciones asimétricas
- **Z-Score**: Apropiado para distribuciones aproximadamente normales

**Variables con más outliers:**
- **MedInc**: Ingreso mediano (distribución altamente sesgada)
- **MEDV**: Precio de viviendas (valores extremos en ambos extremos)
- **Population**: Población (concentración en ciertas áreas)

### Análisis de Correlaciones

![Matriz de Correlaciones](../assets/california-housing-correlations.png)
*Matriz de correlaciones entre variables principales del dataset*

**Correlaciones más significativas:**
- `MedInc` ↔ `MEDV`: Correlación positiva fuerte (0.69)
- `AveRooms` ↔ `MEDV`: Correlación positiva moderada (0.53)
- `Population` ↔ `AveOccup`: Correlación negativa moderada (-0.42)

### Distribuciones Principales

![Distribuciones](../assets/california-housing-distributions.png)
*Distribuciones de las variables más importantes del dataset*

**Características observadas:**
- `MEDV`: Distribución sesgada a la derecha (precios altos menos frecuentes)
- `MedInc`: Distribución altamente sesgada (ingresos extremos)
- `AveRooms`: Distribución aproximadamente normal
- `Population`: Distribución con picos en áreas densamente pobladas

### Análisis por Ubicación

![Análisis por Barrios](../assets/california-housing-neighborhoods.png)
*Precio mediano de viviendas por ubicación geográfica*

**Patrones identificados:**
- San Francisco: Precios más altos (área metropolitana premium)
- Los Angeles: Variabilidad alta en precios
- Sacramento: Precios más estables y accesibles

## 🛠️ Estrategias de Imputación

### Metodología Anti-Leakage

1. **Split de datos** antes de cualquier imputación
2. **Fit imputers** solo en conjunto de entrenamiento
3. **Transform** en validación y test usando parámetros del train
4. **Documentación** de todas las decisiones de imputación

### Estrategias por Tipo de Variable

- **Numéricas**: Mediana (robusta a outliers)
- **Categóricas**: Moda (mantiene consistencia)
- **Flags de imputación**: Indicadores para valores imputados

## 📈 Insights y Conclusiones

### 1. **Patrones de Missing Data**
- **AveOccup**: MCAR - distribución aleatoria sin sesgos
- **AveRooms**: MAR - relacionado con antigüedad de edificios
- **MEDV**: MNAR - valores altos menos reportados

### 2. **Impacto de Outliers**
- **MedInc**: Distribución altamente sesgada con valores extremos
- **MEDV**: Precios extremos en ambos extremos de la distribución
- **Population**: Concentración de población en áreas específicas

### 3. **Consideraciones Éticas**
- **Sesgos socioeconómicos**: Imputación puede afectar grupos demográficos
- **Transparencia**: Documentación de todas las decisiones metodológicas
- **Reproducibilidad**: Pipelines automatizados y versionados

### 4. **Robustez del Pipeline**
- **Anti-leakage**: Prevención de data leakage en validación
- **Reproducibilidad**: Proceso automatizado y documentado
- **Escalabilidad**: Aplicable a otros datasets inmobiliarios

## 🔗 Recursos y Referencias

- **Scikit-learn Documentation**: Datasets and Missing Data
- **Pandas Documentation**: Data Cleaning and Missing Data
- **Seaborn Gallery**: Statistical Data Visualization
- **Boston Housing Dataset**: Original Research Paper

---

*Este análisis demuestra la aplicación de técnicas avanzadas de calidad de datos en un contexto inmobiliario alternativo, manteniendo la rigurosidad metodológica y considerando aspectos éticos del dominio.*
