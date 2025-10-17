# ⚙️ Feature Engineering
{{ reading_time() }}
---

## 📊 Visualizaciones de Feature Engineering

### **🏥 Heart Disease - Feature Scaling**

![Análisis de Escalas](../../assets/heart_disease_scale_analysis.png)
*Distribuciones de variables médicas mostrando escalas problemáticas*

![Boxplots por Feature](../../assets/heart_disease_boxplots.png)
*Boxplots comparativos antes y después del escalado*

![Comparación de Scalers](../../assets/heart_disease_scalers_comparison.png)
*Comparación de StandardScaler, MinMaxScaler y RobustScaler*

![Transformaciones Avanzadas](../../assets/heart_disease_transformations_comparison.png)
*PowerTransformer, QuantileTransformer y Log Transform*

![Experimento de Data Leakage](../../assets/heart_disease_data_leakage_experiment.png)
*Comparación crítica de metodologías con y sin data leakage*

---

### **🔧 Encoding Avanzado**

![Cardinalidad de Variables Categóricas](../../assets/cardinalidad_variables_cat.png)
*Análisis de cardinalidad en variables categóricas*

![Análisis de Features Codificadas](../../assets/analisis_de_features_codificadas.png)
*Distribuciones de variables después del encoding*

![Comparación de Métodos de Encoding](../../assets/comparacion_metodos_de_encoding.png)
*One-Hot Encoding vs Target Encoding vs Label Encoding*

---

### **📈 Transformaciones de Datos**

![Distribuciones de Features Derivadas](../../assets/derived-features-distributions.png)
*Distribuciones de variables transformadas y derivadas*

![Comparación de Transformaciones](../../assets/power-transformer-comparison.png)
*PowerTransformer: Antes vs Después*

![Quantile Transformer](../../assets/quantile-transformer-comparison.png)
*QuantileTransformer: Normalización de distribuciones*

![Log Transform](../../assets/log-transform-lot-area.png)
*Transformación logarítmica aplicada*

---

### **🔍 Selección de Features**

![Top Features Más Importantes](../../assets/Top_Features_mas_importantes.png)
*Ranking de features por importancia*

![Comparación de Importancia por Método](../../assets/comparacion_importancia_por_metodo.png)
*Mutual Information vs Random Forest*

---

## 🎯 Técnicas de Feature Engineering Aplicadas

### **📏 Escalado y Normalización**
- **StandardScaler**: Normalización Z-score
- **MinMaxScaler**: Escalado a rango [0,1]
- **RobustScaler**: Escalado robusto a outliers
- **PowerTransformer**: Transformación de potencia (Yeo-Johnson)

### **🔄 Encoding de Variables Categóricas**
- **One-Hot Encoding**: Variables dummy
- **Label Encoding**: Codificación ordinal
- **Target Encoding**: Codificación por media del target
- **Frequency Encoding**: Codificación por frecuencia

### **📊 Transformaciones de Distribuciones**
- **Log Transform**: Reducción de asimetría
- **QuantileTransformer**: Normalización de distribuciones
- **Box-Cox Transform**: Normalización paramétrica
- **Reciprocal Transform**: Transformación inversa

### **🎯 Selección de Features**
- **Mutual Information**: Dependencia estadística
- **Random Forest**: Importancia por reducción de impureza
- **Correlation Analysis**: Análisis de correlaciones
- **Variance Threshold**: Eliminación de baja varianza

---

## 🔬 Experimentos Críticos

### **⚠️ Data Leakage Prevention**
- **Split-then-scale**: División antes del escalado
- **Pipeline con CV**: Cross-validation con pipelines
- **Comparación de metodologías**: Validación de resultados

### **📈 Performance Impact**
- **Before vs After**: Comparación de métricas
- **Model Performance**: Impacto en modelos ML
- **Computational Efficiency**: Eficiencia computacional

---

## 💡 Insights de Feature Engineering

### **✅ Mejores Prácticas Identificadas:**
- **RobustScaler** es más efectivo con outliers
- **PowerTransformer** normaliza mejor distribuciones sesgadas
- **Pipeline con CV** previene data leakage efectivamente
- **Target Encoding** es superior para variables categóricas de alta cardinalidad

### **⚠️ Cuidados Especiales:**
- **Data leakage** puede invalidar completamente los resultados
- **Outliers** requieren técnicas robustas de escalado
- **High cardinality** necesita encoding especializado
- **Feature selection** debe validarse con múltiples métodos

---

<div style="text-align: center; margin: 40px 0; padding: 20px; background: #e3f2fd; border-radius: 8px;">
  <h3 style="margin: 0; color: #1976d2;">📚 Ver Proyectos Completos</h3>
  <p style="margin: 10px 0 0 0; color: #666;">
    <a href="../../exploraciones-extra/06b-feature-scaling-heart-disease/">Heart Disease Scaling</a> | 
    <a href="../../portfolio/06-feature-scaling-anti-leakage-pipeline/">Feature Scaling Pipeline</a> | 
    <a href="../../portfolio/09-encoding-avanzado-target-encoding/">Advanced Encoding</a>
  </p>
</div>
