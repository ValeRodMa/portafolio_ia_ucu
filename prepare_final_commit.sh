#!/bin/bash
# Script para preparar el commit final
# NO EJECUTAR hasta que el usuario lo indique

echo "📦 Preparando commit final..."

# 1. Remover chatbot del .gitignore temporalmente para poder agregarlo
echo "🔧 Ajustando .gitignore para incluir chatbot..."
sed -i.bak '/^chatbot\/$/d' .gitignore

# 2. Agregar todos los archivos modificados
echo "➕ Agregando archivos modificados..."
git add .gitignore
git add docs/acerca.md
git add docs/portfolio/15-google-cloud-intro.md
git add docs/portfolio/16-cloud-dataprep.md
git add docs/portfolio/index.md
git add docs/recursos.md
git add docs/ruta-de-aprendizaje.md
git add mkdocs.yml

# 3. Agregar nuevos assets
echo "🖼️  Agregando nuevos assets..."
git add docs/assets/Sentinel2_SantaLucia_2023.tif
git add docs/assets/satelital14b_*.png
git add docs/assets/ut5-*.png

# 4. Agregar chatbot completo (forzando porque estaba en .gitignore)
echo "🤖 Agregando chatbot..."
git add -f chatbot/

# 5. Verificar qué se va a commitear
echo ""
echo "📋 Archivos preparados para commit:"
git status --short

echo ""
echo "✅ Todo listo para commit!"
echo "📝 Mensaje de commit sugerido:"
echo ""
echo "feat: commit final del portfolio - incluye chatbot, UT5 y actualizaciones completas"
echo ""
echo "⚠️  IMPORTANTE: Este script NO hace el commit todavía."
echo "   Cuando estés listo, ejecuta: git commit -m 'feat: commit final del portfolio - incluye chatbot, UT5 y actualizaciones completas'"

