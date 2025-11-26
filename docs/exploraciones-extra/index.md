# 🚀 Exploraciones Extra: Investigando + Datasets
Esta sección presenta **exploraciones adicionales** con datasets alternativos.

---

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0;">
  <div style="padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #e8f5e8 100%); border-radius: 12px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
  <div style="font-size: 2.5em; color: #4caf50; margin-bottom: 5px;">8</div>
  <div style="font-size: 1.1em; color: #2e7d32; font-weight: bold;">Exploraciones</div>
  <div style="font-size: 0.9em; color: #666;">Completadas</div>
  </div>
  
  <div style="padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #fff3e0 100%); border-radius: 12px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    <div style="font-size: 2.5em; color: #ff9800; margin-bottom: 5px;">36</div>
    <div style="font-size: 1.1em; color: #f57c00; font-weight: bold;">Visualizaciones</div>
    <div style="font-size: 0.9em; color: #666;">Generadas</div>
  </div>
</div>

---

## Proyectos de Exploración

### **🍷 [Análisis del Wine Quality Dataset](01b-wine-quality-analysis/)**

**Dataset**: Wine Quality (UCI ML Repository) - 1,599 muestras de vino tinto con 11 variables fisicoquímicas y una variable objetivo de calidad (3-8). Incluye propiedades como acidez, alcohol, sulfatos y densidad que determinan la calidad del vino.

**Enfoque**: Análisis exploratorio completo aplicando técnicas EDA para identificar patrones fisicoquímicos que influyen en la calidad del vino.

### **🏠 [Missing Data Detective - California Housing](05b-california-housing-missing-data/)**

**Dataset**: California Housing (Scikit-learn) - 20,640 muestras de viviendas en California (1990) con 8 variables inmobiliarias. Incluye ingreso mediano, edad de viviendas, número de habitaciones, población y ubicación geográfica.

**Enfoque**: Análisis forense de datos faltantes y outliers aplicando técnicas de calidad de datos con consideraciones éticas. Se comenzó a utilizar el dataset de Boston Housing, pero a mitad del análisis se encontró documentación que incluía problemas éticos en dicho dataset (asunciones sobre segregación racial).

### **🏥 [Feature Scaling & Anti-Leakage Pipeline - Heart Disease](06b-feature-scaling-heart-disease/)**

**Dataset**: Heart Disease (UCI ML Repository) - 297 registros de pacientes con 13 variables médicas. Incluye edad, colesterol, presión arterial, frecuencia cardíaca y otros indicadores médicos para predicción de enfermedad cardíaca.

**Enfoque**: Replicación del proyecto de Feature Scaling aplicando técnicas de escalado (StandardScaler, MinMaxScaler, RobustScaler) y experimento crítico de data leakage con datos médicos reales.

### **💳 [Feature Importance Analysis - Credit Card Fraud](08b-feature-importance-credit-card-fraud/)**

**Dataset**: Credit Card Fraud Detection (Kaggle/UCI ML Repository) - 284,807 transacciones con 30 variables financieras. Incluye 28 features anonimizadas (V1-V28), Amount, Time y Class para detección de fraude en tarjetas de crédito.

**Enfoque**: Replicación del análisis de importancia de features aplicando Mutual Information y Random Forest con SMOTE para manejar el desbalance extremo (0.172% de fraude) en datos financieros.

### **👔 [Encoding Avanzado - Employee Attrition](09b-encoding-employee-attrition/)**

**Dataset**: Employee Attrition (IBM HR Analytics) - 1,470 empleados con información completa de recursos humanos. Incluye variables categóricas como Department, JobRole, EducationField, BusinessTravel y otras para predicción de rotación de personal.

**Enfoque**: Replicación del análisis de encoding avanzado aplicando Label Encoding, One-Hot Encoding y Target Encoding en el contexto de recursos humanos, comparando técnicas para variables categóricas de alta cardinalidad.

### **🗺️ [Geoanálisis urbano - Montevideo](12b-geoanalisis-montevideo/)**

**Dataset**: Barrios de Montevideo (Uruguay) - 18 barrios con datos demográficos y de servicios públicos. Incluye población, viviendas, solicitudes de servicios y cobertura de transporte público para análisis geoespacial comparativo.

**Enfoque**: Aplicación del mismo pipeline geoespacial implementado en CABA a un contexto urbano diferente (Montevideo), validando la universalidad de técnicas de CRS, normalizaciones, joins espaciales y visualizaciones coropléticas.

### **📈 [Temporal Feature Engineering - Stock Prices](11b-temporal-features-stock-prices/)**

**Dataset**: Precios de acciones S&P 500 (AAPL, MSFT, GOOGL, AMZN, TSLA, META, NVDA, JPM) - Datos históricos 2022-2024 con precios diarios, volumen y retornos. Incluye múltiples acciones para análisis temporal comparativo en mercados financieros.

**Enfoque**: Aplicación del mismo pipeline de temporal feature engineering implementado en e-commerce a datos financieros, validando la universalidad de técnicas de lag features, rolling/expanding windows, time window aggregations y encoding cíclico en diferentes dominios temporales.

### **🖼️ [Preprocesamiento de Imágenes - Dataset Alternativo](13b-preprocesamiento-imagenes-alternativo/)**

**Dataset**: Imágenes de naturaleza, texturas y arquitectura (scikit-image) - 6 imágenes diferentes incluyendo moon, text, chelsea, brick, grass y hubble_deep_field. Incluye diferentes tipos de texturas y características visuales para análisis de preprocesamiento comparativo.

**Enfoque**: Aplicación del mismo pipeline de preprocesamiento de imágenes implementado en la práctica original a un dataset alternativo, validando la universalidad de técnicas de contraste (CLAHE), suavizado (bilateral), detección de features (ORB/SIFT) y métricas de QA en diferentes tipos de imágenes.

