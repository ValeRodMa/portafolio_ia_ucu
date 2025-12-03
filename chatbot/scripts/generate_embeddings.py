#!/usr/bin/env python3
"""
Script para generar embeddings usando OpenAI API.
"""

import os
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno
load_dotenv()

# Rutas
ROOT_DIR = Path(__file__).parent.parent.parent
DATA_DIR = ROOT_DIR / "chatbot" / "data"
EMBEDDINGS_DIR = ROOT_DIR / "chatbot" / "embeddings"

# Inicializar cliente OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY no encontrada en .env")

client = OpenAI(api_key=api_key)

def generate_embeddings():
    """Genera embeddings para todos los chunks de contenido."""
    EMBEDDINGS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Cargar chunks
    chunks_file = DATA_DIR / "content_chunks.json"
    if not chunks_file.exists():
        print("❌ No se encontró content_chunks.json. Ejecuta primero extract_content.py")
        return
    
    with open(chunks_file, 'r', encoding='utf-8') as f:
        chunks = json.load(f)
    
    print(f"📊 Generando embeddings para {len(chunks)} chunks...")
    
    embeddings_data = []
    
    # Procesar en batches pequeños para evitar rate limits
    # Reducir batch size para respetar límite de 40k tokens/min
    batch_size = 20  # Reducido de 100 a 20
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i+batch_size]
        batch_texts = [chunk["content"] for chunk in batch]
        
        try:
            # Generar embeddings
            response = client.embeddings.create(
                model="text-embedding-3-small",
                input=batch_texts
            )
            
            # Guardar embeddings
            for j, embedding in enumerate(response.data):
                chunk = batch[j]
                embeddings_data.append({
                    "id": chunk["id"],
                    "embedding": embedding.embedding,
                    "content": chunk["content"],
                    "metadata": chunk["metadata"]
                })
            
            print(f"  ✅ Procesados {min(i+batch_size, len(chunks))}/{len(chunks)} chunks")
            
            # Rate limiting más generoso
            time.sleep(2)  # Aumentado a 2 segundos entre batches
            
        except Exception as e:
            print(f"  ❌ Error en batch {i//batch_size + 1}: {e}")
            # Si es rate limit, esperar más tiempo
            if "rate_limit" in str(e).lower() or "429" in str(e):
                print(f"  ⏳ Esperando 10 segundos por rate limit...")
                time.sleep(10)
            continue
    
    # Guardar embeddings
    embeddings_file = EMBEDDINGS_DIR / "embeddings.json"
    with open(embeddings_file, 'w', encoding='utf-8') as f:
        json.dump(embeddings_data, f, ensure_ascii=False)
    
    print(f"\n✅ Embeddings generados: {len(embeddings_data)} embeddings guardados")
    print(f"📁 Archivo: {embeddings_file}")
    
    # Calcular costo estimado
    total_tokens = sum(len(chunk["content"].split()) for chunk in chunks)
    estimated_cost = (total_tokens / 1_000_000) * 0.02
    print(f"💰 Costo estimado: ${estimated_cost:.4f} USD")

if __name__ == "__main__":
    generate_embeddings()

