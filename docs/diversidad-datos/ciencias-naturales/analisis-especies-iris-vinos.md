# 🍷 Análisis de Especies: Iris → Vinos

{{ reading_time() }}

*Adaptando la metodología de clasificación multiclase del dataset Iris al análisis químico de vinos italianos, descubriendo cómo las características químicas pueden revelar el origen geográfico de cada cosecha.*

---

## 📋 **Metadatos del Proyecto**

- **Metodología base**: Clasificación multiclase (Práctica Iris)
- **Dataset nuevo**: UCI Wine Dataset
- **Dominio**: Ciencias Naturales / Enología
- **Técnicas**: EDA, Clasificación, Análisis Químico
- **Estado**: 🚧 En desarrollo

---

## 🎯 **El Desafío: Química vs Morfología**

### **🔄 Adaptación Metodológica**
Mientras que el dataset Iris se basa en **mediciones morfológicas** (longitud y ancho de pétalos y sépalos), el dataset de vinos utiliza **características químicas** (alcohol, ácidos, fenoles, etc.). Esta diferencia fundamental requiere adaptar nuestro enfoque de análisis.

### **📊 Comparación de Datasets**

| **Aspecto** | **Iris Dataset** | **Wine Dataset** |
|-------------|-----------------|------------------|
| **Tipo de datos** | Morfológicos | Químicos |
| **Variables** | 4 (longitud/ancho) | 13 (composición química) |
| **Clases** | 3 especies | 3 regiones italianas |
| **Interpretación** | Biológica | Química/Geográfica |

---

## 🧪 **Dataset: UCI Wine Dataset**

### **📈 Características del Dataset**
- **178 muestras** de vinos italianos
- **13 variables químicas** medidas por análisis químico
- **3 clases** correspondientes a diferentes regiones de Italia
- **Fuente**: UCI Machine Learning Repository

### **🔬 Variables Químicas**
1. **Alcohol**: Contenido alcohólico (%)
2. **Malic Acid**: Ácido málico (g/l)
3. **Ash**: Cenizas (g/l)
4. **Alcalinity of Ash**: Alcalinidad de cenizas
5. **Magnesium**: Magnesio (mg/l)
6. **Total Phenols**: Fenoles totales (mg/l)
7. **Flavanoids**: Flavonoides (mg/l)
8. **Nonflavanoid Phenols**: Fenoles no flavonoides (mg/l)
9. **Proanthocyanins**: Proantocianidinas (mg/l)
10. **Color Intensity**: Intensidad del color
11. **Hue**: Matiz
12. **OD280/OD315**: Relación de absorbancia
13. **Proline**: Prolina (mg/l)

---

## 🔍 **Análisis Exploratorio Adaptado**

### **📊 Visualizaciones Químicas**
- **Distribuciones químicas**: Histogramas de cada componente
- **Pair plots químicos**: Relaciones entre variables químicas
- **Box plots por región**: Comparación química entre regiones italianas
- **Heatmap de correlaciones**: Correlaciones entre componentes químicos

### **🧪 Insights Químicos Únicos**
- **Perfiles químicos regionales**: Características distintivas de cada región
- **Correlaciones químicas**: Relaciones entre diferentes componentes
- **Identificación de marcadores**: Variables más distintivas por región

---

## 🎯 **Objetivos Específicos**

### **🔬 Análisis Químico**
- Identificar los **perfiles químicos** distintivos de cada región
- Analizar las **correlaciones** entre diferentes componentes químicos
- Determinar qué **variables químicas** son más predictivas del origen

### **🌍 Análisis Geográfico**
- Explorar las **diferencias regionales** en la composición química
- Identificar **patrones geográficos** en las características del vino
- Relacionar **terroir** con composición química

### **🤖 Clasificación Adaptada**
- Aplicar **algoritmos de clasificación** al contexto químico
- Comparar **rendimiento** con el análisis morfológico del Iris
- Evaluar la **transferibilidad** de técnicas entre dominios

---

## 📊 **Metodología Adaptada**

### **🔄 Proceso de Adaptación**
1. **Análisis exploratorio químico**: EDA específico para datos químicos
2. **Normalización química**: Adaptación de escalado para variables químicas
3. **Clasificación química**: Aplicación de algoritmos al contexto químico
4. **Validación geográfica**: Verificación de resultados con conocimiento del dominio

### **🧪 Técnicas Específicas**
- **Análisis de componentes principales (PCA)**: Reducción de dimensionalidad química
- **Análisis discriminante**: Identificación de variables más distintivas
- **Clustering químico**: Agrupación basada en similitud química

---

## 🎯 **Insights Esperados**

### **🍷 Enología**
- **Perfiles químicos regionales** distintivos
- **Correlaciones químicas** entre componentes
- **Marcadores químicos** del terroir italiano

### **🔬 Ciencia de Datos**
- **Transferibilidad** de técnicas entre dominios
- **Adaptación metodológica** a nuevos tipos de datos
- **Comparación** entre análisis morfológico y químico

---

## 📈 **Próximos Pasos**

### **🚧 En Desarrollo**
- [ ] Carga y exploración inicial del dataset
- [ ] Análisis exploratorio químico
- [ ] Visualizaciones adaptadas al contexto químico
- [ ] Aplicación de técnicas de clasificación

### **🎯 Próximas Fases**
- [ ] Análisis de componentes principales
- [ ] Comparación con resultados del Iris
- [ ] Insights específicos del dominio enológico
- [ ] Documentación de adaptaciones metodológicas

---

*Este proyecto demuestra cómo las técnicas fundamentales de clasificación pueden adaptarse de la biología morfológica a la química analítica, revelando la versatilidad de las herramientas de ciencia de datos.*
