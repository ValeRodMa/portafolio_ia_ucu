# 🚀 Exploraciones Extra: Investigando + Datasets
Esta sección presenta **exploraciones adicionales** con datasets alternativos.

---

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0;">
  <div style="padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #e8f5e8 100%); border-radius: 12px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
  <div style="font-size: 2.5em; color: #4caf50; margin-bottom: 5px;">4</div>
  <div style="font-size: 1.1em; color: #2e7d32; font-weight: bold;">Exploraciones</div>
  <div style="font-size: 0.9em; color: #666;">Completadas</div>
  </div>
  
  <div style="padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #fff3e0 100%); border-radius: 12px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    <div style="font-size: 2.5em; color: #ff9800; margin-bottom: 5px;">16</div>
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

