#!/bin/bash

# Script para configurar el entorno de desarrollo del portafolio
echo "🚀 Configurando entorno de desarrollo para el portafolio..."

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -r requirements.txt

echo "✅ ¡Entorno configurado!"
echo ""
echo "Para usar el portafolio:"
echo "1. Activa el entorno: source venv/bin/activate"
echo "2. Ejecuta el servidor: mkdocs serve"
echo "3. Visita: http://127.0.0.1:8000"
echo ""
echo "Para desarrollar:"
echo "- Edita archivos en docs/"
echo "- Crea entradas en docs/portfolio/"
echo "- Haz git add, commit y push para desplegar"
