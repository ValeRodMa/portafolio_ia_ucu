# Temporal Feature Engineering: análisis temporal con precios de acciones

<a href="../../assets/Practica_11b_Temporal_Features_Stock_Prices.ipynb" download="Practica_11b_Temporal_Features_Stock_Prices.ipynb">

📓 **Descargar Jupyter Notebook Completo**

</a>

{{ reading_time() }}
---
- **Autor**: Valentín Rodríguez
- **Fecha**: Noviembre 2025
- **Unidad Temática**: UT3: Feature Engineering (Dataset Alternativo)
- **Entorno**: Python + Pandas + yfinance + Scikit-learn + Matplotlib + Seaborn
- **Dataset**: Precios de acciones S&P 500 (AAPL, MSFT, GOOGL, AMZN, TSLA, META, NVDA, JPM) - 2022-2024

---

## 📋 Descripción General

Esta práctica representa una **versión alternativa** del análisis de temporal feature engineering, utilizando **precios de acciones** en lugar del dataset de e-commerce original. El objetivo es demostrar la versatilidad y aplicabilidad universal de las técnicas temporales aplicando la misma metodología a un dominio financiero diferente.

## 🎯 Objetivos Principales

- **Aplicar pipeline completo** de temporal feature engineering a datos financieros
- **Validar metodología** de lag features, rolling/expanding windows y encoding cíclico en mercados financieros
- **Comparar resultados** entre diferentes acciones y períodos temporales
- **Demostrar universalidad** de técnicas temporales independientemente del dominio

## 🔧 Tecnologías y Herramientas

- **Python** con bibliotecas especializadas:
  - `yfinance`: Descarga de datos históricos de acciones
  - `pandas`: Manipulación y análisis de datos temporales
  - `numpy`: Operaciones numéricas y encoding cíclico
  - `scikit-learn`: Modelos de ML y validación temporal
  - `matplotlib` y `seaborn`: Visualización de series temporales

## 📊 Dataset y Metodología

**Dataset:** Precios de acciones S&P 500 - Múltiples empresas (2022-2024)

- **Acciones analizadas:** AAPL, MSFT, GOOGL, AMZN, TSLA, META, NVDA, JPM
- **Período:** 2022-01-01 a 2024-01-01 (2 años de datos)
- **Variables principales:** Precio (Open, High, Low, Close), Volumen, Retornos diarios
- **Fuente:** Yahoo Finance vía yfinance

### Acciones Analizadas

| Acción | Sector | Características |
|--------|--------|-----------------|
| AAPL | Tecnología | Alta capitalización, estabilidad |
| MSFT | Tecnología | Líder en software y cloud |
| GOOGL | Tecnología | Búsqueda y publicidad digital |
| AMZN | E-commerce | Retail y cloud computing |
| TSLA | Automotriz | Volatilidad alta, crecimiento |
| META | Tecnología | Redes sociales y metaverso |
| NVDA | Semiconductores | IA y chips |
| JPM | Finanzas | Banca de inversión |

## 🔍 Análisis Temporal Implementado

### 1. Exploración temporal inicial

- Análisis de distribuciones de precios y retornos
- Patrones por día de semana y mes
- Estadísticas básicas de volatilidad

![Distribuciones temporales](../assets/temporal11b_exploration_distributions.png)
*Análisis inicial: precios por acción, distribución de retornos, volumen por día de semana y retornos por mes*

### 2. Lag Features

- Lag features de precios (1, 2, 3, 7 días anteriores)
- Lag features de retornos y volumen
- Captura de valores históricos para predicción

### 3. Rolling Window Features

- Medias móviles de precios (7d, 30d)
- Volatilidad rolling (std de retornos)
- Máximos y mínimos en ventanas móviles

![Rolling window features](../assets/temporal11b_rolling_features.png)
*Precio actual vs medias móviles y volatilidad rolling - Captura de tendencias recientes*

### 4. Expanding Window Features

- Medias históricas acumuladas desde el inicio
- Retornos promedio históricos
- Comportamiento acumulado vs tendencias recientes

![Rolling vs Expanding](../assets/temporal11b_rolling_vs_expanding.png)
*Comparación de rolling mean (tendencia reciente) vs expanding mean (comportamiento histórico acumulado)*

### 5. Time Window Aggregations

- Agregaciones por ventanas temporales específicas (7d, 30d, 90d)
- Medias de precios y retornos acumulados por ventana
- Detección de cambios de tendencia a diferentes escalas

![Time window aggregations](../assets/temporal11b_time_windows.png)
*Precio vs medias de ventanas temporales y retornos acumulados - Análisis multi-escala*

### 6. Encoding Cíclico

- Encoding cíclico para día de semana (sin/cos)
- Encoding cíclico para mes (sin/cos)
- Captura de patrones estacionales

![Encoding cíclico](../assets/temporal11b_cyclic_encoding.png)
*Representación cíclica de día de semana y mes - Preservación de relaciones temporales*

### 7. Modelo y Evaluación

- Target binario: subida/bajada de precio al día siguiente
- Random Forest con validación temporal
- Análisis de importancia de features temporales

![Importancia de features](../assets/temporal11b_feature_importance.png)
*Top 15 features más importantes - Evaluación del impacto de features temporales*

## 📈 Insights y Conclusiones

### 1. **Efectividad de Lag Features**

- **Precios históricos**: Lag features de precio son predictores fuertes en mercados financieros
- **Retornos históricos**: Retornos pasados muestran autocorrelación significativa
- **Volumen histórico**: Patrones de volumen ayudan a predecir movimientos de precio

### 2. **Rolling Windows en Finanzas**

- **Medias móviles**: Capturan tendencias a corto y mediano plazo
- **Volatilidad rolling**: Identifica períodos de alta/baja volatilidad
- **Máximos/mínimos**: Detectan niveles de soporte y resistencia

### 3. **Expanding Windows**

- **Comportamiento histórico**: Proporciona contexto de largo plazo
- **Retornos acumulados**: Miden performance histórica
- **Comparación con rolling**: Rolling captura tendencias recientes, expanding comportamiento general

### 4. **Time Window Aggregations**

- **Multi-escala**: Ventanas de 7d, 30d, 90d capturan diferentes patrones temporales
- **Retornos acumulados**: Útiles para identificar períodos de ganancia/pérdida sostenida
- **Cambios de tendencia**: Detectan cambios en diferentes escalas temporales

### 5. **Encoding Cíclico**

- **Día de semana**: Captura efectos de "Monday effect" y otros patrones semanales
- **Mes**: Identifica estacionalidad en retornos (efecto de fin de año, etc.)
- **Preservación de relaciones**: Encoding cíclico mantiene proximidad temporal (Lunes cerca de Domingo)

### 6. **Aplicabilidad Metodológica**

- **Técnicas universales**: El pipeline funciona en diferentes dominios temporales
- **Validación temporal**: Crítica para evitar data leakage en datos financieros
- **Features más importantes**: Lag features y rolling windows son los más predictivos

## 🔄 Comparación con la Práctica Original

### Similitudes Metodológicas

1. **Pipeline idéntico**: Misma secuencia de operaciones (lag → rolling → expanding → cíclico)
2. **Técnicas aplicadas**: Lag features, rolling/expanding windows, encoding cíclico funcionan igual
3. **Validación temporal**: Mismo enfoque de prevención de data leakage

### Diferencias Observadas

- **Dominio**: Finanzas vs e-commerce tienen diferentes patrones temporales
- **Target**: Predicción de movimiento de precio vs recompra de cliente
- **Features más importantes**: En finanzas, lag features son más críticos que en e-commerce
- **Escalas temporales**: Finanzas requiere análisis más granular (días vs semanas)

## 🛠️ Implementación Técnica

### Pipeline de Análisis

```python
# 1. Lag features
df['close_lag_1'] = df.groupby('stock')['close'].shift(1)

# 2. Rolling windows
df['rolling_close_mean_7'] = (
    df.groupby('stock')['close']
    .shift(1)
    .rolling(window=7, min_periods=1)
    .mean()
)

# 3. Expanding windows
df['expanding_close_mean'] = (
    df.groupby('stock')['close']
    .shift(1)
    .expanding(min_periods=1)
    .mean()
)

# 4. Encoding cíclico
df['dow_sin'] = np.sin(2 * np.pi * df['day_of_week'] / 7)
df['dow_cos'] = np.cos(2 * np.pi * df['day_of_week'] / 7)
```

### Visualizaciones Implementadas

- **Series temporales**: Precios y retornos a lo largo del tiempo
- **Distribuciones**: Retornos, volumen, patrones temporales
- **Comparativas**: Rolling vs expanding, diferentes ventanas temporales
- **Importancia de features**: Ranking de features temporales más predictivos

## 📚 Aprendizajes Adquiridos

1. **Universalidad**: Las técnicas temporales son aplicables a cualquier dominio con datos temporales
2. **Lag features críticos**: En finanzas, valores históricos son predictores muy fuertes
3. **Rolling windows efectivos**: Capturan tendencias recientes críticas en análisis financiero
4. **Encoding cíclico útil**: Preserva relaciones temporales y captura estacionalidad
5. **Validación temporal**: Fundamental para evitar data leakage en cualquier dominio temporal

## 🔗 Recursos y Referencias

- **yfinance Documentation**: Descarga de datos históricos de acciones
- **Pandas Time Series**: Rolling, expanding, shift operations
- **Temporal Feature Engineering**: Best practices y prevención de data leakage
- **Financial Time Series Analysis**: Patrones temporales en mercados financieros

---

*Este análisis demuestra la versatilidad y aplicabilidad universal de las técnicas de temporal feature engineering, aplicando la misma metodología rigurosa a un dominio diferente (finanzas vs e-commerce), validando la robustez del pipeline implementado.*