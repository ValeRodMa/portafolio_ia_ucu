---
title: "Desplegando mi Portfolio: de código local a GitHub Pages con MkDocs"
date: 2025-08-13
---

# Desplegando mi Portfolio: de código local a GitHub Pages con MkDocs

{{ reading_time() }}

## Contexto
Guía completa para crear y publicar un portfolio académico utilizando GitHub Pages, desde la configuración inicial hasta el despliegue automático.

## Objetivos
- Configurar un repositorio desde el template oficial
- Activar GitHub Pages con despliegue automático
- Completar el contenido mínimo requerido
- Publicar el portfolio en línea

## Actividades (con tiempos estimados)

### **1. Crear tu repo desde el template (5–10 min)**

1. Abrí el template: https://github.com/ucudal/ia-portfolio-template
2. Clic en **Use this template** → **Create a new repository**
3. Completa:
   - **Owner**: tu usuario personal
   - **Repository name**: algo simple, p. ej. `ia-portfolio` o `portfolio-ia`
   - **Public**
4. Clic en **Create repository**


**Pistas:**
- Elegí un nombre corto y sin espacios; activá Public para poder publicar Pages
- Agregá una descripción breve del repo; no hace falta licencias adicionales si el template ya las trae

### **2. Activar GitHub Pages (5 min)**

1. En tu nuevo repo, ve a **Settings** → **Pages**
2. En **Build and deployment**:
   - **Source**: GitHub Actions
3. Guardá
4. En **Actions** (pestaña del repo), verificá que corra el workflow de deploy (tarda 1–3 min)
5. La URL quedará como: `https://<tu-usuario>.github.io/<tu-repo>/` (aparece en la sección Pages cuando termina el deploy)

**Pistas:**
- Si ves 404, esperá unos minutos y recargá; confirmá que la rama y ruta de deploy sean las del workflow
- Recordá que la URL incluye el nombre del repo (`/<tu-repo>/`)

### **3. Completar el contenido mínimo hoy**

Editá el contenido del repo (README y/o las páginas indicadas en el template). Sugerencias concretas:

#### **A. Portada / About**
- Nombre, breve bio (2–3 líneas), links (LinkedIn/GitHub)
- Objetivo del curso en tus palabras (1–2 líneas)

#### **B. Prácticas relacionadas**
- Link a la práctica 1: Exploración del dataset Iris
- Link a la práctica 2: Análisis exploratorio del dataset Iris
- Capturas o gráficos clave (pairplot, correlaciones, boxplots)
- 3–5 hallazgos iniciales y cómo cargaste los datos (seaborn/sklearn/Kaggle/URL)

**Pistas:**
- Usá links relativos entre prácticas: `[Iris](01-exploracion-iris.md)`
- Estructurá con encabezados (`##`), listas y tablas simples cuando ayude

#### **C. Visualizaciones e insights de Iris**
- Incluye 1–2 visualizaciones destacadas de tu EDA (ej.: pairplot y heatmap)
- Redacta 2–3 observaciones concretas por gráfico
- Lista breve de próximos pasos/mejoras para el análisis

#### **D. "Próximos pasos" (backlog personal)**
!!! tip "Tip"
    El template trae secciones prediseñadas, y de ejemplo, usalas para ayudarte.

### **4. Publicar cambios (5 min)**
1. Hacé commit + push de tus cambios
2. Verificá que corra el workflow de GitHub Actions
3. Probá tu sitio: `https://<tu-usuario>.github.io/<tu-repo>/`

**Pistas:**
- Mensaje de commit sugerido: `feat: publicar estructura inicial del portafolio`
- Si el deploy falla, abrí el job en Actions y buscá errores de permisos o rutas

### **5. Entrega en WebAsignatura (2 min)**

1. En la tarea "Portafolio – Práctica 3", pega la URL pública de tu portafolio (la de GitHub Pages)
2. Asegurate de que cualquier persona con el link pueda verlo



## ✅ Checklist

- [X] Repo creado desde template (no fork)
- [X] Pages activado por Actions y deploy exitoso
- [X] Secciones mínimas completadas y visibles
- [X] Links a la práctica de exploración de Iris funcionan

## 🧯 Errores comunes

- **El deploy falla** → abre la pestaña Actions y mira el log del workflow
- **No ves el sitio** → revisá la configuración de Pages y esperá 2–3 minutos

## Evidencias
- Repositorio creado y configurado correctamente
- GitHub Pages activado y funcionando
- Contenido mínimo publicado y accesible
- URL del portfolio funcionando públicamente


### **Lo más desafiante**
- **Configuración inicial de Pages**: Entender la diferencia entre deployment sources
- **Debugging de workflows**: Interpretar los logs de GitHub Actions cuando algo falla
- **Gestión de URLs**: Asegurar que todos los links relativos funcionen correctamente

