#!/usr/bin/env python3
"""
Script para actualizar completamente el chatbot:
1. Calcula métricas del portfolio
2. Extrae contenido de todos los archivos
3. Genera embeddings

Este script debe ejecutarse cada vez que se actualiza el portfolio.
"""

import sys
from pathlib import Path

# Añadir el directorio de scripts al path
SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPTS_DIR))

# Importar los módulos
from calculate_metrics import calculate_portfolio_metrics
from extract_content import extract_portfolio_content
from generate_embeddings import generate_embeddings

def main():
    """Ejecuta el pipeline completo de actualización."""
    print("=" * 60)
    print("🚀 ACTUALIZACIÓN COMPLETA DEL CHATBOT")
    print("=" * 60)
    print()
    
    # Paso 1: Calcular métricas
    print("📊 PASO 1/3: Calculando métricas del portfolio...")
    print("-" * 60)
    try:
        calculate_portfolio_metrics()
        print("✅ Métricas calculadas correctamente\n")
    except Exception as e:
        print(f"❌ Error calculando métricas: {e}\n")
        return False
    
    # Paso 2: Extraer contenido
    print("📄 PASO 2/3: Extrayendo contenido...")
    print("-" * 60)
    try:
        extract_portfolio_content()
        print("✅ Contenido extraído correctamente\n")
    except Exception as e:
        print(f"❌ Error extrayendo contenido: {e}\n")
        return False
    
    # Paso 3: Generar embeddings
    print("🧠 PASO 3/3: Generando embeddings...")
    print("-" * 60)
    try:
        generate_embeddings()
        print("✅ Embeddings generados correctamente\n")
    except Exception as e:
        print(f"❌ Error generando embeddings: {e}\n")
        return False
    
    print("=" * 60)
    print("✅ ACTUALIZACIÓN COMPLETA EXITOSA")
    print("=" * 60)
    print()
    print("El chatbot ahora puede responder preguntas sobre:")
    print("  - Contenido de todas las prácticas")
    print("  - Métricas y estadísticas del portfolio")
    print("  - Entrada más larga, más gráficas, etc.")
    print("  - Datasets y tecnologías utilizadas")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

