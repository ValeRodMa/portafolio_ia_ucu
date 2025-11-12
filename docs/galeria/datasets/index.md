# 📈 Datasets Especializados
---

## 🎯 Visualizaciones por Dominio de Aplicación

### **🏥 Dominio Médico - Heart Disease**

![Análisis de Escalas Médicas](../../assets/heart_disease_scale_analysis.png)
*Variables médicas: edad, colesterol, presión arterial, frecuencia cardíaca*

![Boxplots Médicos](../../assets/heart_disease_boxplots.png)
*Distribuciones de indicadores de salud cardiovascular*

![Scalers Médicos](../../assets/heart_disease_scalers_comparison.png)
*Escalado de variables médicas con diferentes técnicas*

![Transformaciones Médicas](../../assets/heart_disease_transformations_comparison.png)
*Normalización de distribuciones médicas*

![Data Leakage Médico](../../assets/heart_disease_data_leakage_experiment.png)
*Prevención de data leakage en datos médicos*

---

### **💳 Dominio Financiero - Credit Card Fraud**

![Distribuciones Financieras](../../assets/credit_card_fraud_distributions.png)
*Distribuciones de Amount, Time y features anonimizadas*

![Comparación Normal vs Fraude](../../assets/credit_card_fraud_class_comparison.png)
*Patrones de comportamiento en transacciones normales vs fraudulentas*

![Importancia Financiera](../../assets/credit_card_fraud_mutual_information.png)
*Features más críticas para detección de fraude*

![Random Forest Financiero](../../assets/credit_card_fraud_random_forest.png)
*Importancia de features en contexto de modelo financiero*

![Comparación de Métodos Financieros](../../assets/credit_card_fraud_methods_comparison.png)
*Validación cruzada de metodologías en datos financieros*

---

### **🍷 Dominio Agrícola - Wine Quality**

![Distribuciones del Vino](../../assets/wine-quality-distributions.png)
*Variables fisicoquímicas del vino tinto*

![Correlaciones del Vino](../../assets/wine-correlation-heatmap.png)
*Relaciones entre acidez, alcohol, sulfatos y calidad*

![Boxplots por Calidad](../../assets/wine-quality-boxplots.png)
*Distribuciones de variables por nivel de calidad*

![Distribución de Calidad](../../assets/wine-quality-distribution.png)
*Distribución de la variable objetivo (calidad 3-8)*

![Relaciones Calidad-Features](../../assets/wine-quality-quality-vs-features.png)
*Impacto de variables fisicoquímicas en la calidad*

![Pairplot del Vino](../../assets/wine-pairplot-analysis.png)
*Análisis multivariado completo del vino*

---

### **🏠 Dominio Inmobiliario - California Housing**

![Distribuciones Inmobiliarias](../../assets/california-housing-distributions.png)
*Variables del mercado inmobiliario de California*

![Correlaciones Inmobiliarias](../../assets/california-housing-correlations.png)
*Relaciones entre precio, ubicación y características*

![Vecindarios de California](../../assets/california-housing-neighborhoods.png)
*Distribución geográfica de precios de viviendas*

![Patrones de Missing Data](../../assets/california-housing-missing-patterns.png)
*Análisis de datos faltantes en el mercado inmobiliario*

![Outliers Inmobiliarios](../../assets/california-housing-outliers-analysis.png)
*Identificación de propiedades atípicas*

---

### **🌺 Dominio Biológico - Iris Dataset**

![Distribuciones Biológicas](../../assets/iris-distributions-individual.png)
*Medidas morfológicas de especies de iris*

![Boxplots por Especie](../../assets/iris-boxplots-species.png)
*Comparación de medidas entre especies*

![Correlaciones Biológicas](../../assets/iris-correlation-heatmap.png)
*Relaciones entre medidas morfológicas*

![Outliers Biológicos](../../assets/iris-outliers-analysis.png)
*Identificación de especímenes atípicos*

![Dashboard Biológico](../../assets/iris-dashboard-complete.png)
*Análisis integral de datos biológicos*

![Pairplot Biológico](../../assets/iris-pairplot-complete.png)
*Análisis multivariado de especies de iris*

![Violin Plots Biológicos](../../assets/iris-violin-plots.png)
*Distribuciones de densidad por especie*

---

### **📺 Dominio de Entretenimiento - Netflix**

![Dashboard de Netflix](../../assets/netflix-dashboard.png)
*Análisis de contenido y tendencias de streaming*

---

### **🖼️ Visión por Computadora - Preprocesamiento UT4**

![Diagnóstico inicial y rango tonal](../../assets/ut5_histograma_camera.png)
*Imagen base y distribución de intensidades en escala de grises*

![Histogramas por canal RGB](../../assets/ut5_hist_rgb.png)
*Comparación de canales para detectar dominancias cromáticas*

![Comparativa de contraste (Original vs Equalize vs CLAHE)](../../assets/ut5_contraste_comparacion.png)
*Ecualización global frente a realce adaptativo de luminancia*

![Suavizado y bordes (Gaussian vs Bilateral + Canny)](../../assets/ut5_suavizado_bordes.png)
*Impacto del suavizado en la detección de contornos confiables*

![Keypoints ORB por variante](../../assets/ut5_orb_keypoints.png)
*Densidad de puntos de interés según preprocesamiento aplicado*

![Matching ORB entre original y CLAHE](../../assets/ut5_orb_matches.png)
*Repetibilidad de features tras realzar contraste local*

![Sensibilidad vs ruido (CLAHE y suavizados)](../../assets/ut5_sensibilidad_ruido.png)
*Barrido de parámetros para equilibrar keypoints y bordes falsos*

![Benchmark ORB vs SIFT](../../assets/ut5_benchmark_orb_sift.png)
*Comparativa de tiempo y matches entre descriptores binarios y flotantes*

![Dashboard de control de calidad](../../assets/ut5_dashboard_qa.png)
*KPIs por imagen y alertas automáticas para monitorear lotes*

---

### **🗺️ Dominio Urbano - Datos Geoespaciales (CABA)**

![Silueta de radios censales de CABA](../../assets/ut4_radios_caba.png)
*Cobertura urbana completa de radios censales en WGS84*

![Densidad de población por km²](../../assets/ut4_densidad_hab_km2.png)
*Coropleta de densidad habitacional tras reproyección a CRS métrico*

![Contactos SUACI per cápita por barrio](../../assets/ut4_suaci_contactos_pc.png)
*Integración de datos ciudadanos con demografía barrial*

![Heatmap hexagonal H3 (res 8)](../../assets/ut4_hex_heatmap.png)
*Tasas per cápita agregadas en hexágonos para comparar hotspots urbanos*

---

## 🎯 Características por Dominio

### **🏥 Datos Médicos**
- **Variables**: Edad, colesterol, presión arterial, ECG
- **Desafíos**: Privacy, interpretabilidad, sesgo médico
- **Técnicas**: Feature scaling, data leakage prevention
- **Aplicación**: Diagnóstico asistido, medicina preventiva

### **💳 Datos Financieros**
- **Variables**: Amount, Time, features anonimizadas
- **Desafíos**: Desbalance extremo, privacidad, fraude
- **Técnicas**: SMOTE, feature importance, detección de anomalías
- **Aplicación**: Detección de fraude, scoring crediticio

### **🍷 Datos Agrícolas**
- **Variables**: Acidez, alcohol, sulfatos, pH
- **Desafíos**: Calidad subjetiva, variabilidad natural
- **Técnicas**: EDA completo, análisis de correlaciones
- **Aplicación**: Control de calidad, mejora de procesos

### **🏠 Datos Inmobiliarios**
- **Variables**: Precio, ubicación, características
- **Desafíos**: Missing data, outliers geográficos
- **Técnicas**: Análisis de missing data, geolocalización
- **Aplicación**: Valuación, análisis de mercado

### **🌺 Datos Biológicos**
- **Variables**: Medidas morfológicas, especies
- **Desafíos**: Clasificación multiclase, outliers naturales
- **Técnicas**: EDA completo, análisis multivariado
- **Aplicación**: Taxonomía, clasificación biológica

### **🗺️ Datos Urbanos**
- **Variables**: Radios censales, contactos ciudadanos, densidad
- **Desafíos**: CRS, joins espaciales, comparabilidad entre zonas
- **Técnicas**: GeoPandas, normalización por superficie, hexgrids H3
- **Aplicación**: Planificación urbana, priorización de servicios

---

## 💡 Insights por Dominio

### **🔍 Patrones Comunes:**
- **Distribuciones normales** en la mayoría de variables
- **Outliers importantes** que requieren análisis especial
- **Correlaciones significativas** entre variables relacionadas
- **Missing data** con patrones específicos por dominio

### **⚙️ Técnicas Específicas:**
- **Médico**: Data leakage prevention, interpretabilidad
- **Financiero**: Desbalance handling, anonimización
- **Agrícola**: EDA exhaustivo, análisis de calidad
- **Inmobiliario**: Missing data analysis, geolocalización
- **Biológico**: Clasificación multiclase, taxonomía
- **Urbano**: Joins espaciales, análisis de densidad, hexbin comparables

### **🎯 Aplicaciones Prácticas:**
- **Diagnóstico médico** asistido por IA
- **Detección de fraude** en tiempo real
- **Control de calidad** en procesos industriales
- **Análisis de mercado** inmobiliario
- **Clasificación taxonómica** automatizada
- **Planificación urbana** basada en evidencia geoespacial

---

<div style="text-align: center; margin: 40px 0; padding: 20px; background: #fff3e0; border-radius: 8px;">
  <h3 style="margin: 0; color: #f57c00;">📚 Ver Proyectos Completos por Dominio</h3>
  <p style="margin: 10px 0 0 0; color: #666;">
    <a href="../../exploraciones-extra/06b-feature-scaling-heart-disease/">🏥 Heart Disease</a> | 
    <a href="../../exploraciones-extra/08b-feature-importance-credit-card-fraud/">💳 Credit Card Fraud</a> | 
    <a href="../../exploraciones-extra/01b-wine-quality-analysis/">🍷 Wine Quality</a><br>
    <a href="../../exploraciones-extra/05b-california-housing-missing-data/">🏠 California Housing</a> | 
    <a href="../../portfolio/01-practica-iris/">🌺 Iris Dataset</a> | 
    <a href="../../portfolio/12-datos-especiales-geoespacial/">🗺️ CABA Geoespacial</a> |
    <a href="../../portfolio/13-preprocesamiento-imagenes/">🖼️ Preprocesamiento de Imágenes</a>
  </p>
</div>
