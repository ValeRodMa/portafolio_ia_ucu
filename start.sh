#!/bin/bash

echo "Iniciando..."
echo "Entrando al proyecto..."
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

echo "🐍 Activando entorno virtual..."
source venv/bin/activate

echo "Iniciando servidor MkDocs..."
echo "Servidor disponible en: http://127.0.0.1:8000/"
echo "Portfolio en: http://127.0.0.1:8000/portfolio/"
echo ""
echo "Para detener el servidor: Ctrl+C"
echo ""
mkdocs serve