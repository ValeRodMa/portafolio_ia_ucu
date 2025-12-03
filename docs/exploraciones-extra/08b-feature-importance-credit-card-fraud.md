# Análisis de Importancia de Features - Credit Card Fraud Detection

<a href="../../assets/Practica08B_Credit_Card_Fraud_Feature_Importance.ipynb" download="Practica08B_Credit_Card_Fraud_Feature_Importance.ipynb">

📓 **Descargar Jupyter Notebook Completo**

</a>

{{ reading_time() }}
---
- **Autor:** Valentín Rodríguez
- **Fecha:** Octubre 2025
- **Unidad Temática:** UT3: Feature Engineering (Dataset Alternativo)
- **Entorno:** Jupyter Notebook + Python (pandas, numpy, matplotlib, seaborn, scikit-learn, imbalanced-learn)
- **Dataset:** Credit Card Fraud Detection (UCI ML Repository) - 284,807 transacciones, 30 variables financieras

---

---

## 📋 Descripción General

Este proyecto replica el **análisis de importancia de features** del proyecto original 08, pero utilizando el dataset de **Credit Card Fraud Detection**. A través de técnicas como Mutual Information y Random Forest, exploramos las variables más críticas para detectar fraude en transacciones de tarjetas de crédito en tiempo real.

## 🎯 Objetivos Principales

- **Evaluar importancia de features** para detección de fraude usando Mutual Information vs Random Forest
- **Analizar distribuciones** de variables financieras anonimizadas (V1-V28) y conocidas (Amount, Time)
- **Identificar patrones** críticos para sistemas de detección en tiempo real
- **Comparar efectividad** de diferentes metodologías en datos financieros desbalanceados
- **Visualizar insights** sobre la importancia de features anonimizadas vs conocidas

## 🔧 Tecnologías y Herramientas

- **Python** con bibliotecas especializadas:
  - `scikit-learn`: Feature selection, Mutual Information, Random Forest
  - `imbalanced-learn`: SMOTE para balanceo de clases
  - `pandas` y `numpy`: Manipulación y análisis de datos
  - `matplotlib` y `seaborn`: Visualización avanzada
  - `scipy.stats`: Análisis estadístico

## 📊 Dataset y Metodología

**Dataset:** Credit Card Fraud Detection (Kaggle/UCI ML Repository)

- **Dimensiones:** 284,807 transacciones con 31 variables
- **Variables analizadas:** 28 features anonimizadas (V1-V28) + Amount + Time + Class
- **Target:** Detección de fraude (0=Normal, 1=Fraude)
- **Desbalance:** 0.172% de transacciones fraudulentas

### Variables Principales Analizadas

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `V1-V28` | Anonimizadas | Features transformadas con PCA (información confidencial) |
| `Time` | Temporal | Segundos transcurridos entre transacción y primera transacción |
| `Amount` | Financiera | Monto de la transacción ($) |
| `Class` | Target | Variable objetivo (0=Normal, 1=Fraude) |

## 🧪 Metodología de Análisis

### 1. **Análisis de Distribuciones**
- Exploración de distribuciones de features anonimizadas (normalizadas)
- Análisis específico de Amount (log-normal) y Time (uniforme)
- Comparación de distribuciones entre transacciones normales y fraudulentas

### 2. **Mutual Information Analysis**
- Cálculo de dependencia estadística entre features y target
- Identificación de features con mayor información mutua
- Análisis de correlaciones no lineales en datos financieros

### 3. **Random Forest Importance**
- Entrenamiento con SMOTE para balancear clases desbalanceadas
- Evaluación de importancia basada en reducción de impureza
- Análisis de performance del modelo en detección de fraude

### 4. **Comparación de Metodologías**
- Correlación entre rankings de Mutual Information y Random Forest
- Identificación de features críticas comunes a ambos métodos
- Recomendaciones para sistemas de producción

## 📊 Resultados y Visualizaciones

### Distribuciones de Features

![Distribuciones de Features](../assets/credit_card_fraud_distributions.png)
*Análisis de distribuciones: Amount (log-normal), Time (uniforme), y features anonimizadas V1, V14*

### Comparación Normal vs Fraude

![Comparación de Clases](../assets/credit_card_fraud_class_comparison.png)
*Distribuciones comparativas entre transacciones normales y fraudulentas*

### Importancia con Mutual Information

![Mutual Information](../assets/credit_card_fraud_mutual_information.png)
*Top 15 features más importantes según Mutual Information (destacando Amount y Time)*

### Importancia con Random Forest

![Random Forest](../assets/credit_card_fraud_random_forest.png)
*Top 15 features más importantes según Random Forest con SMOTE*

### Comparación de Metodologías

![Comparación de Métodos](../assets/credit_card_fraud_methods_comparison.png)
*Comparación directa entre Mutual Information y Random Forest (top 15 features normalizadas)*

## 🔍 Hallazgos Clave

### **1. Características del Dataset**
- **Altamente desbalanceado:** Solo 0.172% de transacciones fraudulentas
- **Features anonimizadas:** V1-V28 contienen patrones críticos para detección
- **Distribuciones específicas:** Amount con distribución log-normal, Time uniforme
- **Contexto financiero:** Amount y Time proporcionan información contextual valiosa

### **2. Importancia de Features**
- **Features anonimizadas:** Dominan el ranking de importancia en ambos métodos
- **Amount:** Variable financiera crítica con alta importancia en ambos rankings
- **Time:** Proporciona contexto temporal importante para detección
- **Patrones ocultos:** Features V1-V28 revelan comportamientos fraudulentos sutiles

### **3. Comparación de Metodologías**
- **Correlación moderada:** Entre Mutual Information y Random Forest
- **Concordancia parcial:** Features críticas identificadas por ambos métodos
- **Complementariedad:** Cada método aporta perspectivas diferentes
- **Validación cruzada:** Necesaria para confirmar importancia de features

## 💻 Código Clave

### **Setup y Carga de Datos**
```python
# Cargar dataset de Credit Card Fraud
df = pd.read_csv('creditcard.csv')

# Preparar features
feature_cols = [f'V{i+1}' for i in range(28)] + ['Time', 'Amount']
X = df[feature_cols]
y = df['Class']

# Escalar datos
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)
```

### **Análisis con Mutual Information**
```python
# Calcular Mutual Information
mi_scores = mutual_info_classif(X_scaled, y, random_state=42)

# Crear ranking
mi_results = pd.DataFrame({
    'Feature': feature_cols,
    'MI_Score': mi_scores
}).sort_values('MI_Score', ascending=False)
```

### **Análisis con Random Forest**
```python
# Balancear con SMOTE
smote = SMOTE(random_state=42)
X_balanced, y_balanced = smote.fit_resample(X_scaled, y)

# Entrenar Random Forest
rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    class_weight='balanced',
    random_state=42
)
rf.fit(X_balanced, y_balanced)

# Obtener importancia
feature_importance = rf.feature_importances_
```

### **Comparación de Métodos**
```python
# Combinar resultados
comparison_df = pd.merge(mi_results, rf_results, on='Feature')

# Normalizar para comparación
comparison_df['MI_Normalized'] = comparison_df['MI_Score'] / comparison_df['MI_Score'].max()
comparison_df['RF_Normalized'] = comparison_df['RF_Importance'] / comparison_df['RF_Importance'].max()

# Calcular correlación
correlation = comparison_df['MI_Normalized'].corr(comparison_df['RF_Normalized'])
```

## 🎯 Conclusiones y Recomendaciones

### **✅ Para Detección de Fraude en Tiempo Real**
- **Priorizar features** en top 10 de AMBOS métodos para máxima confiabilidad
- **Features anonimizadas V1-V28** son críticas y contienen patrones ocultos
- **Amount** proporciona contexto financiero esencial para validación
- **Time** puede revelar patrones temporales de comportamiento fraudulento

### **✅ Para Selección de Features**
- **Mutual Information:** Mejor para detectar dependencias no lineales y patrones sutiles
- **Random Forest:** Mejor para evaluar importancia en contexto de modelo real
- **Validación cruzada:** Usar ambos métodos para confirmar robustez de features
- **Balanceo:** SMOTE esencial para entrenar modelos efectivos con datos desbalanceados

### **✅ Para Sistemas de Producción**
- **Monitoreo continuo** de top 15 features más importantes
- **Drift detection** en features críticas para mantener efectividad
- **Balance precisión vs velocidad** en sistemas de detección en tiempo real
- **Interpretabilidad** limitada por features anonimizadas, pero efectividad alta

### **🔬 Insights Técnicos**
- **Desbalance extremo:** Requiere técnicas especializadas como SMOTE
- **Features anonimizadas:** Contienen información valiosa a pesar de la falta de interpretabilidad
- **Correlación moderada:** Indica que ambos métodos aportan perspectivas complementarias
- **Contexto financiero:** Amount y Time son críticos para validación de transacciones

## 📚 Referencias y Recursos

- [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- [Scikit-learn Feature Selection](https://scikit-learn.org/stable/modules/feature_selection.html)
- [Imbalanced-learn SMOTE](https://imbalanced-learn.org/stable/over_sampling.html#smote-adasyn)
- [Random Forest Feature Importance](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html)
- *Feature Engineering for ML* - Cap. 5: Feature Selection

---

## 🎉 Impacto del Proyecto

Este análisis demuestra la **replicabilidad exitosa** del proyecto original 08 aplicado a un dominio completamente diferente. Los resultados validan que:

1. **Las metodologías son robustas** y funcionan en diferentes tipos de datos
2. **El análisis de importancia de features** es crítico para sistemas financieros
3. **La combinación de métodos** (MI + RF) proporciona validación cruzada valiosa
4. **Los datos anonimizados** pueden contener información valiosa para ML

**Aplicación práctica:** Este tipo de análisis es fundamental para sistemas de detección de fraude en bancos, fintechs y procesadores de pagos, donde la velocidad y precisión son críticas para prevenir pérdidas financieras.