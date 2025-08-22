---
title: "Entrada de Familiarización - Proyecto inicial"
date: 2025-08-13
---

# Entrada de Familiarización - Proyecto inicial
{{ reading_time() }}

## Contexto
Primera actividad práctica del curso de **Ingeniería de Datos**, diseñada para familiarizarse con las herramientas y metodologías que utilizaremos durante todo el semestre. Esta entrada marca el inicio del portfolio académico que documentará mi progreso y aprendizajes.

## Objetivos
- Configurar correctamente el entorno de desarrollo local con **MkDocs** y **Python**
- Familiarizarme con el flujo de trabajo **Git** y **GitHub Pages**
- Establecer la estructura base del portfolio académico

## Actividades (con tiempos estimados)
- **Configurar el repositorio y entorno local** — 45 min
- **Instalar dependencias (MkDocs, Material Theme)** — 15 min  
- **Crear estructura de directorios y archivos base** — 30 min
- **Configurar GitHub Actions para despliegue automático** — 20 min
- **Personalizar tema y estilos** — 40 min
- **Crear primera entrada de prueba** — 30 min
- **Documentar proceso y reflexionar** — 20 min

**Total estimado: 3 horas**

## Desarrollo

### **Configuración del Entorno**
1. **Creación del repositorio** en GitHub con nombre `portafolio_ia_ucu`
2. **Clonado local** y configuración de Git
3. **Instalación de MkDocs Material** y plugins necesarios

### 📁 **Estructura del Proyecto**
```
portafolio_ia_ucu/
├── docs/
│   ├── index.md              # Página principal
│   ├── acerca.md             # Información personal
│   ├── recursos.md           # Enlaces útiles
│   ├── assets/               # Imágenes y recursos
│   └── portfolio/            # Entradas del portfolio
├── mkdocs.yml                # Configuración del sitio
└── requirements.txt          # Dependencias Python
```

### **Personalización**
- **Tema Material** con colores personalizados
- **Logo personalizado** con iconos seleccionados 
- **Navegación optimizada** con secciones claras
- **Favicon personalizado** para identidad visual
- **Diseño responsive** para múltiples dispositivos

### **Despliegue Automático**
- Configuración de **GitHub Actions** 
- Despliegue automático en **GitHub Pages** con cada push
- URL final: `https://valerodma.github.io/portafolio_ia_ucu/`

## Evidencias
- **Repositorio funcionando**: [GitHub Repository](https://github.com/ValeRodMa/portafolio_ia_ucu)
- **Sitio web desplegado**: [Portfolio en vivo](https://valerodma.github.io/portafolio_ia_ucu/)
- **Entorno local configurado**: Servidor de desarrollo en `http://127.0.0.1:8000`
- **Workflow de GitHub Actions**: Despliegue automático funcionando
- **Estructura base completa**: Todas las secciones principales creadas

## Reflexión

### **Lo más valioso**
- **Herramientas profesionales**: MkDocs Material, me permite obtener un portfolio profesional.
- **Base sólida**: La estructura creada servirá para todo el curso

### **Lo más desafiante**
- **Configuración inicial de dependencias**: Resolver conflictos de versiones de Python
- **GitHub Actions debugging**: Entender los errores de despliegue y modo strict
- **Personalización de CSS**: Lograr el diseño deseado sin romper el diseño responsive de la web
- **Gestión de rutas**: Resolver problemas de paths


