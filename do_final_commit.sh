#!/bin/bash
# Script para ejecutar el commit final
# Este script se ejecutará cuando el usuario lo indique

set -e  # Salir si hay errores

echo "🚀 Iniciando commit final..."

# 1. Remover chatbot del .gitignore temporalmente para poder agregarlo
echo "🔧 Ajustando .gitignore para incluir chatbot..."
if grep -q "^chatbot/$" .gitignore; then
    sed -i.bak '/^chatbot\/$/d' .gitignore
fi

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

# 3. Agregar nuevos assets (si existen)
echo "🖼️  Agregando nuevos assets..."
[ -f "docs/assets/Sentinel2_SantaLucia_2023.tif" ] && git add docs/assets/Sentinel2_SantaLucia_2023.tif
[ -f "docs/assets/satelital14b_indices_calculation.png" ] && git add docs/assets/satelital14b_indices_calculation.png
[ -f "docs/assets/satelital14b_prediction_model.png" ] && git add docs/assets/satelital14b_prediction_model.png
[ -f "docs/assets/satelital14b_time_series.png" ] && git add docs/assets/satelital14b_time_series.png
[ -f "docs/assets/ut5-cloud-dataprep-merge-columns.png" ] && git add docs/assets/ut5-cloud-dataprep-merge-columns.png
[ -f "docs/assets/ut5-cloud-dataprep-pipeline.png" ] && git add docs/assets/ut5-cloud-dataprep-pipeline.png
[ -f "docs/assets/ut5-cloud-dataprep-suggestions.png" ] && git add docs/assets/ut5-cloud-dataprep-suggestions.png
[ -f "docs/assets/ut5-google-cloud-console.png" ] && git add docs/assets/ut5-google-cloud-console.png
[ -f "docs/assets/ut5-google-cloud-lab-completion.png" ] && git add docs/assets/ut5-google-cloud-lab-completion.png
[ -f "docs/assets/ut5-google-cloud-self-paced-labs.png" ] && git add docs/assets/ut5-google-cloud-self-paced-labs.png

# 4. Agregar chatbot completo (forzando porque estaba en .gitignore)
echo "🤖 Agregando chatbot..."
git add -f chatbot/

# 5. Verificar qué se va a commitear
echo ""
echo "📋 Archivos que se van a commitear:"
git status --short

echo ""
echo "💾 Ejecutando commit..."
git commit -m "feat: commit final del portfolio - incluye chatbot, UT5 y actualizaciones completas

- Agregado chatbot completo con backend Flask y frontend
- Actualizadas prácticas 15 y 16 de UT5 (Google Cloud y Cloud Dataprep)
- Agregados nuevos assets e imágenes de UT5
- Actualizado índice del portfolio y recursos
- Actualizada ruta de aprendizaje
- Mejoras en documentación general"

echo ""
echo "✅ Commit realizado exitosamente!"
echo "📤 Para hacer push: git push origin main"


