# Práctica 6: Feature Scaling & Anti-Leakage Pipeline
{{ reading_time() }}
---
- **Autores**: Joaquín Batista, Milagros Cancela, Valentín Rodríguez, Alexia Aurrecoechea, Nahuel López (G1)
- **Fecha**: Agosto 2025
- **Unidad Temática**: UT2 - Calidad & Ética
- **Tipo**: Práctica Guiada
- **Entorno**: Python + Pandas + Scikit-learn + Seaborn
- **Dataset**: Ames Housing Dataset (2930 registros, 82 variables)

---

## 📋 Descripción General

Esta práctica se enfoca en uno de los aspectos más críticos del preprocessing en Machine Learning: **Feature Scaling** y la prevención de **Data Leakage**. A través de una exploración práctica con el dataset Ames Housing, investigamos diferentes técnicas de escalado, transformaciones avanzadas, y la implementación de pipelines robustos.

## 🎯 Objetivos Principales

- **Identificar features** del dataset Ames que requieren escalado y entender por qué
- **Experimentar** con MinMaxScaler, StandardScaler y RobustScaler en datos reales
- **Descubrir el impacto** del escalado en diferentes algoritmos de ML
- **Comparar pipelines** con y sin data leakage para evidenciar las diferencias
- **Implementar transformadores avanzados** y evaluar su efectividad

## 🔧 Tecnologías y Herramientas

- **Python** con bibliotecas especializadas:
  - `scikit-learn`: Preprocessing, pipelines, y validación cruzada
  - `pandas` y `numpy`: Manipulación y análisis de datos
  - `matplotlib` y `seaborn`: Visualización de distribuciones y transformaciones
  - `scipy.stats`: Análisis estadístico de asimetría

## 📊 Dataset y Metodología

**Dataset:** Ames Housing (continuación de prácticas anteriores)

- **Dimensiones:** 2,930 registros × 82 columnas

- **Variables numéricas:** 39 columnas con escalas muy diferentes

- **Target:** SalePrice (predicción de precios de casas)


**Acceso al notebook completo:** [Práctica 6 - Feature Scaling & Anti-Leakage Pipeline](../assets/Practica_6_Feature_Scaling_Anti-Leakage_Pipeline.ipynb)


### Análisis de Escalas Problemáticas

| Variable | Rango (min–max) | Ratio | ¿Problemática? |
|----------|-----------------|-------|----------------|
| **Lot Area** | 1,300 – 215,245 | 165.57 | ✅ Muy sesgada, outliers extremos |
| **SalePrice** | 12,789 – 755,000 | 59.04 | ✅ Rango amplio, afecta distancias |
| **Gr Liv Area** | 334 – 5,642 | 16.89 | ⚠️ Moderadamente problemática |
| **Overall Qual** | 1 – 10 | 10.00 | ❌ Escala controlada |

## 🧪 Experimentos Realizados

### 1. Comparación de Scalers Tradicionales

**StandardScaler vs MinMaxScaler vs RobustScaler**

- Análisis de impacto en detección de outliers

- Evaluación con diferentes algoritmos (KNN, SVM, Linear Regression)

- **Resultado:** StandardScaler mostró mejor consistencia para modelos lineales


### 2. Transformaciones Avanzadas

#### PowerTransformer (Yeo-Johnson)
- **Objetivo:** Reducir asimetría y estabilizar varianza
- **Resultado en SalePrice:** Skew 1.74 → 0.002, Outliers IQR 137 → 59
- **Conclusión:** Excelente para variables con fuerte sesgo

#### QuantileTransformer
- **Objetivo:** Mapear a distribución normal por cuantiles
- **Ventaja:** Muy robusto a outliers extremos
- **Limitación:** Puede "aplastar" extremos con pocos datos

#### Log Transform (log1p seguro)
- **Aplicado a:** Lot Area (skew = 12.814)
- **Resultado:** Skew 12.814 → -0.498
- **Implementación:** Manejo seguro de valores ≤ 0 con shift automático

### 3. Orden de Operaciones: Outliers vs Escalado

**Hallazgo clave:** El escalado modifica la detección de outliers

- **Antes del escalado:** IQR detecta 137 outliers

- **Después del escalado:** IQR detecta 107 outliers

- **Recomendación:** Tratar outliers antes del escalado


## ⚠️ Data Leakage: El Experimento Crítico

### Comparación de 3 Métodos

| Método | RMSE | Descripción |
|--------|------|-------------|
| **Con Leakage** | 32,185 | Escalar todo → Split (INCORRECTO) |
| **Sin Leakage Manual** | 32,287 | Split → Escalar (CORRECTO) |
| **Pipeline + CV** | 30,651 | Anti-leakage automático (ÓPTIMO) |

**Impacto del Leakage:** ΔRMSE ≈ -1,534 (mejora significativa con pipeline)

### ¿Por qué Pipeline es Superior?

```python
# Pipeline Anti-Leakage
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', KNeighborsRegressor())
])

# En cada fold de CV:
# 1. Scaler se ajusta SOLO con datos de training
# 2. Se evalúa en datos completamente no vistos
# 3. Evita fuga sutil de información estadística
```

## 🏆 Pipeline Recomendado Final

```python
mi_mejor_pipeline = Pipeline([
    ('preprocessor', FunctionTransformer(func=safe_log1p)),  # Para variables sesgadas
    ('scaler', StandardScaler()),                            # Escalado estándar
    ('model', LinearRegression())                            # Modelo baseline
])
```

**Validación:** R² = 0.776 ± 0.033 (5-fold CV) - Estable y robusto

## 📊 Análisis Visual de Transformaciones

### Distribuciones y Outliers
![Distribuciones](../assets/feature-distributions.png)
*Distribuciones de variables clave: SalePrice y Lot Area muestran fuerte asimetría, mientras Overall Qual es aproximadamente normal.*

![Boxplots](../assets/feature-boxplots.png)
*Boxplots revelan outliers extremos en precios y áreas, confirmando la necesidad de transformaciones.*

### Efectividad de Transformadores

![Log Transform](../assets/log-transform-lot-area.png)
*Log transform en Lot Area: reduce skew de 12.8 a -0.5, normalizando la distribución.*

![PowerTransformer](../assets/power-transformer-comparison.png)
*PowerTransformer (Yeo-Johnson): transforma SalePrice a distribución casi perfectamente normal (skew ≈ 0.002).*

![QuantileTransformer](../assets/quantile-transformer-comparison.png)
*QuantileTransformer: fuerza normalidad perfecta mapeando cuantiles empíricos a distribución normal.*

## 📈 Resultados y Conclusiones

### Principales Hallazgos

1. **StandardScaler** fue el más consistente para el dataset Ames Housing
2. **PowerTransformer (Yeo-Johnson)** superó significativamente a scalers básicos en variables sesgadas
3. **Log transform** es altamente efectivo para variables como precios y áreas
4. **Data leakage** tiene impacto medible y significativo en el rendimiento
5. **Pipeline** es esencial para validación honesta y deployment robusto

### Recomendaciones Prácticas

- **Para variables sesgadas:** Aplicar log transform antes del escalado
- **Para outliers:** Detectar y tratar antes de cualquier transformación
- **Para validación:** Usar siempre Pipeline con cross-validation
- **Para producción:** Nunca aplicar transformaciones antes del split

## 🔍 Reflexiones Técnicas

**¿Cuándo usar cada transformador?**
- **StandardScaler:** Modelos lineales, datos aproximadamente normales

- **RobustScaler:** Presencia moderada de outliers

- **PowerTransformer:** Fuerte asimetría, necesidad de normalidad

- **QuantileTransformer:** Distribuciones multimodales o colas extremas


**Orden óptimo de operaciones:**
1. Detección/tratamiento de outliers

2. Transformaciones de forma (log, Yeo-Johnson)

3. Escalado (Standard, MinMax, Robust)

4. Validación con Pipeline


## 🎓 Aprendizajes Clave

Esta práctica consolidó conceptos fundamentales sobre:
- La criticidad del **orden de operaciones** en preprocessing

- El impacto real del **data leakage** en métricas de evaluación

- La superioridad de **transformadores avanzados** para datos no ideales

- La importancia de **Pipeline** para workflows reproducibles y robustos


---