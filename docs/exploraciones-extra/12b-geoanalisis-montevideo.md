# Geoanálisis urbano con GeoPandas: análisis de densidad y servicios en Montevideo
{{ reading_time() }}
---
- **Autor**: Valentín Rodríguez
- **Fecha**: Noviembre 2025
- **Unidad Temática**: UT4: Datos Especiales (Dataset Alternativo)
- **Entorno**: Python + GeoPandas + Shapely + Contextily + Folium + MapClassify
- **Dataset**: Barrios de Montevideo (Uruguay) con datos demográficos y de servicios públicos sintéticos

---

## 📋 Descripción General

Esta práctica representa una **versión alternativa** del análisis geoespacial implementado en CABA, utilizando datos de **barrios de Montevideo (Uruguay)**. El objetivo es demostrar la versatilidad y aplicabilidad universal de las técnicas geoespaciales aplicando la misma metodología a un contexto urbano diferente.

## 🎯 Objetivos Principales

- **Aplicar pipeline geoespacial** completo a un dataset alternativo (Montevideo)
- **Validar metodología** de CRS, normalizaciones y joins espaciales en otro contexto
- **Comparar patrones urbanos** entre CABA y Montevideo
- **Demostrar universalidad** de técnicas geoespaciales independientemente del dominio

## 🔧 Tecnologías y Herramientas

- **Python** con bibliotecas especializadas:
  - `geopandas` y `shapely`: Manipulación y análisis geoespacial
  - `contextily`: Tiles de contexto para mapas
  - `folium`: Visualizaciones interactivas
  - `mapclassify`: Esquemas de clasificación para coropletas
  - `pandas` y `numpy`: Análisis de datos

## 📊 Dataset y Metodología

**Dataset:** Barrios de Montevideo (Uruguay) - Dataset sintético basado en estructura real

- **Dimensiones:** 18 barrios con datos demográficos y de servicios
- **Variables principales:** Población, viviendas, solicitudes de servicios públicos
- **Fuente:** Datos sintéticos generados para demostración metodológica

**Acceso al notebook completo:** [Práctica 12B - Geoanálisis Montevideo](../assets/Practica_12b_Montevideo_Geospatial_Analysis.ipynb)

### Barrios Analizados

| Barrio | Población | Comuna | Características |
|--------|-----------|--------|-----------------|
| Ciudad Vieja | 12,000 | 1 | Zona histórica y administrativa |
| Centro | 35,000 | 1 | Área comercial y de servicios |
| Cordón | 28,000 | 2 | Zona residencial y universitaria |
| Pocitos | 45,000 | 2 | Zona costera y residencial premium |
| Buceo | 18,000 | 2 | Zona costera y comercial |
| Malvín | 32,000 | 2 | Zona residencial y costera |
| Punta Carretas | 15,000 | 1 | Zona comercial y residencial |
| Parque Rodó | 22,000 | 1 | Zona recreativa y residencial |
| Palermo | 25,000 | 1 | Zona residencial |
| Aguada | 30,000 | 1 | Zona residencial y comercial |
| Prado | 20,000 | 3 | Zona residencial |
| Paso Molino | 18,000 | 3 | Zona residencial |
| Belvedere | 15,000 | 3 | Zona residencial |
| La Teja | 28,000 | 3 | Zona residencial e industrial |
| Cerro | 35,000 | 3 | Zona residencial |
| Casavalle | 40,000 | 4 | Zona residencial |
| Manga | 22,000 | 4 | Zona residencial |
| Tres Ombúes | 18,000 | 4 | Zona residencial |

## 🔍 Análisis Geoespacial Implementado

### 1. Limpieza geométrica y proyección

- Lectura de datos geoespaciales de barrios de Montevideo
- Conversión a CRS proyectado (`.to_crs(epsg=3857)`) para garantizar áreas y distancias consistentes
- Cálculo de área en m² y densidad por km² como indicadores derivados

![Silueta de barrios de Montevideo](../assets/ut4b_radios_mvd.png){ width="520" }
*Mapa base de barrios de Montevideo en WGS84*

### 2. Visualización coroplética

- Mapas simples con `GeoDataFrame.plot` usando esquemas `quantiles`
- Incorporación de tiles de contexto (`CartoDB.Positron`) vía `contextily`
- Análisis de zonas de mayor densidad poblacional

![Coropleta de densidad habitacional en Montevideo](../assets/ut4b_densidad_hab_km2_mvd.png){ width="520" }
*Densidad de población por barrio en Montevideo (hab/km²)*

![Densidad con tiles de contexto](../assets/ut4b_densidad_contexto_mvd.png){ width="520" }
*Densidad poblacional con tiles de contexto para mejor interpretación espacial*

### 3. Attribute join y métricas per cápita

- Unión (`merge`) con tabla de servicios públicos para enriquecer con métricas de atención ciudadana
- Cálculo de indicadores normalizados (`solicitudes_pc`) y ranking de barrios con mayor carga relativa
- Comparación de demanda de servicios ajustada por población

![Solicitudes de servicios públicos per cápita](../assets/ut4b_solicitudes_pc_mvd.png){ width="520" }
*Solicitudes de servicios públicos per cápita por barrio en Montevideo*

### 4. Joins espaciales: Transporte público

- Conteo de estaciones de transporte por barrio usando `gpd.sjoin`
- Cálculo de densidad de estaciones por km²
- Visualización de cobertura de transporte público

![Cobertura de transporte público](../assets/ut4b_cobertura_transporte_mvd.png){ width="520" }
*Cobertura de transporte público por barrio con estaciones marcadas*

## 📈 Insights y Conclusiones

### 1. **Patrones de Densidad Poblacional**

- **Barrios centrales (Comuna 1)**: Ciudad Vieja, Centro, Palermo concentran mayor densidad
- **Zona costera (Comuna 2)**: Pocitos, Buceo, Malvín muestran alta densidad residencial
- **Zonas periféricas (Comunas 3-4)**: Menor densidad pero mayor extensión territorial

### 2. **Demanda de Servicios Públicos**

- **Patrón similar a CABA**: Barrios centrales muestran mayor demanda per cápita
- **Normalización efectiva**: La métrica per cápita revela patrones que no son visibles con valores absolutos
- **Hotspots identificados**: Ciudad Vieja y Centro concentran mayor actividad administrativa

### 3. **Cobertura de Transporte**

- **Distribución desigual**: Mayor concentración de estaciones en barrios centrales
- **Accesibilidad**: Barrios periféricos tienen menor densidad de estaciones por km²
- **Oportunidades de mejora**: Identificación de zonas con brechas de accesibilidad

### 4. **Aplicabilidad Metodológica**

- **Técnicas universales**: El pipeline geoespacial es aplicable a cualquier ciudad
- **CRS proyectado**: Fundamental para comparaciones métricas consistentes
- **Normalizaciones**: Evitan sesgos por tamaño absoluto de población o área
- **Spatial joins**: Permiten enriquecer análisis demográficos con infraestructura

## 🔄 Comparación con CABA

### Similitudes Metodológicas

1. **CRS proyectado (EPSG:3857)**: Mismo estándar para áreas y distancias comparables
2. **Normalización por km² y per cápita**: Misma estrategia para evitar sesgos
3. **Spatial joins**: Misma técnica para enriquecer datos demográficos
4. **Visualizaciones con contexto**: Mismo uso de tiles para mejor interpretación

### Diferencias Observadas

- **Estructura urbana**: Montevideo tiene una distribución más dispersa que CABA
- **Densidad**: Barrios centrales concentran densidad pero con patrones diferentes
- **Servicios**: Patrones similares de demanda per cápita en zonas centrales
- **Escala**: Montevideo es una ciudad más pequeña que CABA

## 🛠️ Implementación Técnica

### Pipeline de Análisis

```python
# 1. Carga y proyección
barrios_mvd = gpd.GeoDataFrame(...)
barrios_mvd_m = barrios_mvd.to_crs(epsg=3857)

# 2. Cálculo de áreas y densidades
barrios_mvd_m["area_m2"] = barrios_mvd_m.geometry.area
barrios_mvd_m["densidad_hab_km2"] = barrios_mvd_m["POBLACION"] / (barrios_mvd_m["area_m2"] / 1e6)

# 3. Attribute join
barrios_mvd_m = barrios_mvd_m.merge(servicios_df, on="BARRIO", how="left")
barrios_mvd_m["solicitudes_pc"] = barrios_mvd_m["total_solicitudes"] / barrios_mvd_m["POBLACION"]

# 4. Spatial join
est_x_barrio = gpd.sjoin(estaciones_mvd, barrios_mvd_m, how="left", predicate="within")
```

### Visualizaciones Implementadas

- **Coropletas**: Mapas temáticos con esquemas de clasificación (quantiles)
- **Mapas con contexto**: Integración de tiles de fondo para mejor interpretación
- **Mapas interactivos**: Visualizaciones con Folium para exploración dinámica

## 📚 Aprendizajes Adquiridos

1. **Universalidad**: Las técnicas geoespaciales son aplicables a cualquier contexto urbano
2. **Metodología consistente**: El mismo pipeline funciona en diferentes ciudades
3. **Normalizaciones críticas**: Evitan sesgos por tamaño absoluto
4. **Spatial joins**: Herramienta poderosa para enriquecer análisis demográficos
5. **Visualización contextual**: Los tiles mejoran significativamente la interpretación

## 🔗 Recursos y Referencias

- **GeoPandas Documentation**: User Guide (Introduction, CRS, Plotting)
- **Kaggle Learn**: Geospatial Analysis
- **Brust, A. V. (2023)**: Ciencia de Datos para Gente Sociable – Cap. 6: Información geográfica y mapas
- **Contextily Documentation**: Adding basemaps to GeoPandas plots

---

*Este análisis demuestra la versatilidad y aplicabilidad universal de las técnicas geoespaciales, aplicando la misma metodología rigurosa a un contexto urbano diferente (Montevideo vs CABA), validando la robustez del pipeline implementado.*

