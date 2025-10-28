# 🎯 Modelos y Evaluación
---

## 📊 Visualizaciones de Modelos y Evaluación

### **💳 Credit Card Fraud - Feature Importance**

![Mutual Information](../../assets/credit_card_fraud_mutual_information.png)
*Top 15 features más importantes según Mutual Information*

![Random Forest Importance](../../assets/credit_card_fraud_random_forest.png)
*Top 15 features más importantes según Random Forest*

![Comparación de Métodos](../../assets/credit_card_fraud_methods_comparison.png)
*Comparación directa entre MI y RF (normalizadas)*

![Distribuciones por Clase](../../assets/credit_card_fraud_class_comparison.png)
*Distribuciones comparativas: Normal vs Fraude*

![Distribuciones de Features](../../assets/credit_card_fraud_distributions.png)
*Análisis de distribuciones en datos financieros*

---

### **⚖️ Bias Detection y Fairness**

![Análisis de Bias por Grupos Raciales](../../assets/bias-analysis-racial-groups.png)
*Análisis de sesgo algorítmico en grupos demográficos*

---

### **📈 Performance y Métricas**

![Comparación de Métodos de Encoding](../../assets/comparacion_metodos_de_encoding.png)
*Impacto del encoding en performance del modelo*

![Comparación de Correlaciones](../../assets/correlaciones-comparison.png)
*Análisis de correlaciones antes y después de transformaciones*

---

## 🎯 Técnicas de Modelado Aplicadas

### **🌲 Algoritmos de Machine Learning**
- **Random Forest**: Importancia de features y clasificación
- **Logistic Regression**: Modelos lineales para clasificación
- **K-Nearest Neighbors**: Clasificación basada en proximidad
- **Support Vector Machine**: Clasificación con márgenes óptimos

### **📊 Evaluación de Modelos**
- **Cross-Validation**: Validación cruzada con k-fold
- **Performance Metrics**: Accuracy, Precision, Recall, F1-Score
- **ROC-AUC**: Análisis de curvas ROC
- **Confusion Matrix**: Matrices de confusión detalladas

### **⚖️ Bias Detection y Fairness**
- **Demographic Parity**: Paridad demográfica
- **Equalized Odds**: Oportunidades igualadas
- **Fairlearn**: Herramientas de fairness en ML
- **Statistical Parity**: Paridad estadística

---

## 🔬 Experimentos de Modelado

### **💳 Credit Card Fraud Detection**
- **Dataset**: 284,807 transacciones (0.172% fraude)
- **Desbalance**: SMOTE para balancear clases
- **Métodos**: Mutual Information + Random Forest
- **Resultado**: Identificación de features críticas

### **🏥 Heart Disease Prediction**
- **Dataset**: 297 registros médicos
- **Objetivo**: Predicción de enfermedad cardíaca
- **Técnicas**: Feature scaling + anti-leakage
- **Resultado**: Pipeline robusto sin data leakage

### **⚖️ Bias Analysis**
- **Enfoque**: Detección de sesgo algorítmico
- **Métricas**: Paridad demográfica y oportunidades igualadas
- **Herramientas**: Fairlearn library
- **Resultado**: Análisis de fairness en modelos

---

## 📊 Métricas y Performance

### **🎯 Métricas de Clasificación**
- **Accuracy**: Precisión general del modelo
- **Precision**: Exactitud en predicciones positivas
- **Recall**: Sensibilidad en detección de casos positivos
- **F1-Score**: Balance entre precision y recall
- **ROC-AUC**: Área bajo la curva ROC

### **📈 Métricas de Fairness**
- **Demographic Parity**: P(Ŷ=1|A=a) = P(Ŷ=1|A=b)
- **Equalized Odds**: P(Ŷ=1|Y=y,A=a) = P(Ŷ=1|Y=y,A=b)
- **Equal Opportunity**: P(Ŷ=1|Y=1,A=a) = P(Ŷ=1|Y=1,A=b)

### **🔍 Feature Importance**
- **Mutual Information**: Dependencia estadística
- **Random Forest**: Reducción de impureza
- **Correlation**: Correlación con target
- **Permutation Importance**: Importancia por permutación

---

## 💡 Insights de Modelado

### **✅ Mejores Prácticas Identificadas:**
- **SMOTE** es esencial para datasets desbalanceados
- **Pipeline con CV** previene data leakage efectivamente
- **Multiple metrics** proporcionan visión completa del performance
- **Feature importance** debe validarse con múltiples métodos

### **⚠️ Desafíos Encontrados:**
- **Desbalance extremo** (0.172% fraude) requiere técnicas especiales
- **Data leakage** puede invalidar completamente los resultados
- **Bias detection** es crítica en aplicaciones reales
- **Feature selection** debe balancear performance vs interpretabilidad

### **🎯 Recomendaciones:**
- **Validación cruzada** siempre con pipelines
- **Múltiples métricas** para evaluación completa
- **Bias analysis** en todos los modelos de producción
- **Feature importance** con validación cruzada de métodos

---

<div style="text-align: center; margin: 40px 0; padding: 20px; background: #fce4ec; border-radius: 8px;">
  <h3 style="margin: 0; color: #c2185b;">📚 Ver Proyectos Completos</h3>
  <p style="margin: 10px 0 0 0; color: #666;">
    <a href="../../exploraciones-extra/08b-feature-importance-credit-card-fraud/">Credit Card Fraud</a> | 
    <a href="../../portfolio/07-bias-detection-fairlearn/">Bias Detection</a> | 
    <a href="../../portfolio/08-feature-importance-analysis/">Feature Importance</a>
  </p>
</div>
