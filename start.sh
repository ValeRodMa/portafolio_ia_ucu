#!/bin/bash

echo "Iniciando..."
echo "Entrando al proyecto..."
cd "/Users/valentin.rodriguez.machado/Library/CloudStorage/OneDrive-Personal/UCU/IA/Ingeniería de Datos/portafolio_ia_ucu"

echo "🐍 Activando entorno virtual..."
source venv/bin/activate

echo "Iniciando servidor MkDocs..."
echo "Servidor disponible en: http://127.0.0.1:8000/"
echo "Portfolio en: http://127.0.0.1:8000/portfolio/"
echo ""
echo "Para detener el servidor: Ctrl+C"
echo ""
mkdocs serve