#!/usr/bin/env python3
"""
Script de prueba para verificar que el chatbot puede responder
preguntas sobre métricas del portfolio.
"""

import os
import sys
from pathlib import Path

# Añadir el directorio backend al path
BACKEND_DIR = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Importar funciones del backend
from app import load_embeddings, search_relevant_chunks

def test_query(query: str, top_k: int = 3):
    """Prueba una consulta y muestra los resultados."""
    print(f"\n{'='*70}")
    print(f"PREGUNTA: {query}")
    print(f"{'='*70}")
    
    # Buscar chunks relevantes
    chunks = search_relevant_chunks(query, top_k=top_k, min_similarity=0.3)
    
    if not chunks:
        print("❌ No se encontraron resultados relevantes")
        return
    
    print(f"✅ Se encontraron {len(chunks)} chunks relevantes:\n")
    
    for i, chunk in enumerate(chunks, 1):
        metadata = chunk['metadata']
        title = metadata.get('title', 'Sin título')
        file_path = metadata.get('file', '')
        content = chunk['content'][:200] + "..." if len(chunk['content']) > 200 else chunk['content']
        
        print(f"[{i}] {title}")
        print(f"    Archivo: {file_path}")
        print(f"    Preview: {content}")
        print()

def main():
    """Ejecuta pruebas de consultas sobre métricas."""
    print("🧪 PRUEBAS DE MÉTRICAS DEL PORTFOLIO")
    print("="*70)
    
    # Cargar embeddings
    print("\n📊 Cargando embeddings...")
    load_embeddings()
    print("✅ Embeddings cargados\n")
    
    # Definir preguntas de prueba
    test_queries = [
        "¿Cuál es la entrada más larga del portfolio?",
        "¿Cuántas gráficas se generaron en total?",
        "¿Qué práctica tiene más imágenes?",
        "¿Cuántas prácticas hay en el portfolio?",
        "¿Qué datasets se utilizaron?",
        "¿Cuál es el promedio de palabras por entrada?",
        "¿Qué tecnologías se usaron?",
    ]
    
    print("Ejecutando consultas de prueba...\n")
    
    for query in test_queries:
        test_query(query, top_k=2)
        input("Presiona Enter para continuar con la siguiente pregunta...")
    
    print("\n" + "="*70)
    print("✅ PRUEBAS COMPLETADAS")
    print("="*70)
    print("\nEl chatbot ahora puede responder preguntas sobre:")
    print("  • Métricas generales del portfolio")
    print("  • Récords y destacados")
    print("  • Datasets y tecnologías utilizadas")
    print("  • Comparativas entre entradas")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Pruebas interrumpidas por el usuario")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

