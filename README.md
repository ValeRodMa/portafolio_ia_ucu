# Portafolio de Ingeniería de IA & Ciencia de Datos: Ingeniería de Datos - 2025

Este repositorio contiene mi **portafolio** del curso de Ingeniería de IA & Ciencia de Datos, construido con **MkDocs + Material** y desplegado automáticamente en GitHub Pages.

## 🚀 Configuración rápida

### Opción 1: Script automático
```bash
chmod +x dev-setup.sh
./dev-setup.sh
```

### Opción 2: Manual
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🖥️ Desarrollo local

```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar servidor de desarrollo
mkdocs serve

# Visitar http://127.0.0.1:8000
```

## 📝 Cómo agregar contenido

1. **Escribe únicamente en `docs/`**
2. **Crea entradas en `docs/portfolio/`** siguiendo `plantilla.md`
3. **Mantén el frontmatter** en cada `.md`:
   ```yaml
   ---
   title: "Título de la página"
   date: YYYY-MM-DD
   ---
   ```
4. **Usa nombres ordenados**: `01-titulo.md`, `02-otro.md`
5. **Enlaces relativos** para recursos locales

## 🔄 Flujo de trabajo

```bash
# 1. Desarrollar localmente
mkdocs serve

# 2. Agregar cambios
git add .

# 3. Hacer commit
git commit -m "Descripción de los cambios"

# 4. Subir a GitHub (dispara despliegue automático)
git push origin main
```

## 🚀 Despliegue

- **Automático**: Cada `push` a `main` ejecuta el build y publica en GitHub Pages
- **GitHub Actions** maneja el despliegue
- **URL del sitio**: Se configura automáticamente en la pestaña Pages del repositorio

## 📁 Estructura del proyecto

```
portafolio_ia_ucu/
├── docs/                    # Contenido del sitio
│   ├── portfolio/          # Entradas del portafolio
│   ├── assets/            # Imágenes y recursos
│   └── *.md              # Páginas principales
├── .github/workflows/     # GitHub Actions
├── venv/                 # Entorno virtual (ignorado)
├── mkdocs.yml           # Configuración de MkDocs
└── requirements.txt     # Dependencias Python
```

## 🛠️ Tecnologías

- **MkDocs**: Generador de sitios estáticos
- **Material Theme**: Tema moderno y responsive
- **GitHub Pages**: Hosting gratuito
- **GitHub Actions**: CI/CD automático
