#!/usr/bin/env python3
"""
API para el chatbot del portfolio.
"""

import os
import json
import numpy as np
from pathlib import Path
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
CORS(app)  # Permitir CORS para el frontend

# Rutas - Compatible con desarrollo y producción
ROOT_DIR = Path(__file__).parent.parent
EMBEDDINGS_DIR = ROOT_DIR / "embeddings"

# Inicializar cliente OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY no encontrada en .env")

client = OpenAI(api_key=api_key)

# Cargar embeddings al iniciar
embeddings_data = None

def load_embeddings():
    """Carga los embeddings desde el archivo JSON."""
    global embeddings_data
    embeddings_file = EMBEDDINGS_DIR / "embeddings.json"
    
    if not embeddings_file.exists():
        print("⚠️  No se encontró embeddings.json. Ejecuta generate_embeddings.py primero")
        return
    
    with open(embeddings_file, 'r', encoding='utf-8') as f:
        embeddings_data = json.load(f)
    
    print(f"✅ Embeddings cargados: {len(embeddings_data)} chunks")

def cosine_similarity(vec1, vec2):
    """Calcula la similitud coseno entre dos vectores."""
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def search_relevant_chunks(query: str, top_k: int = 5):
    """Busca los chunks más relevantes para una consulta."""
    if not embeddings_data:
        return []
    
    import re
    
    # Detectar si pregunta por número de práctica (múltiples patrones)
    practica_num = None
    # Patrón 1: "práctica 11", "practico 11"
    match1 = re.search(r'practic[aoí]\s*(\d+)', query.lower())
    # Patrón 2: "11 práctica", "11 práctico"
    match2 = re.search(r'(\d+)\s*practic[aoí]', query.lower())
    # Patrón 3: Solo número después de "la" o "el"
    match3 = re.search(r'(?:la|el)\s+.*?(\d+)', query.lower())
    
    if match1:
        practica_num = match1.group(1)
    elif match2:
        practica_num = match2.group(1)
    elif match3:
        practica_num = match3.group(1)
    
    # BÚSQUEDA HÍBRIDA: Primero buscar por número exacto, luego por similitud
    exact_matches = []
    if practica_num:
        # Buscar chunks que coincidan exactamente con el número de práctica
        for item in embeddings_data:
            file_path = item["metadata"].get("file", "").lower()
            # Buscar patrones: 11-, -11-, 11_, práctica 11, etc.
            if (f"{practica_num.zfill(2)}-" in file_path or 
                f"-{practica_num}-" in file_path or
                f"{practica_num.zfill(2)}_" in file_path or
                f"practica-{practica_num}" in file_path or
                f"practica_{practica_num}" in file_path):
                exact_matches.append(item)
        
        # Si encontramos matches exactos, ordenarlos por relevancia semántica
        if exact_matches:
            # Generar embedding de la query para ordenar los matches exactos
            try:
                enhanced_query = f"práctica {practica_num} temporal feature engineering datos transaccionales " + query
                response = client.embeddings.create(
                    model="text-embedding-3-small",
                    input=[enhanced_query]
                )
                query_embedding = response.data[0].embedding
                
                # Ordenar matches exactos por similitud semántica
                exact_with_sim = []
                for item in exact_matches:
                    similarity = cosine_similarity(query_embedding, item["embedding"])
                    exact_with_sim.append((similarity, item))
                
                exact_with_sim.sort(key=lambda x: x[0], reverse=True)
                print(f"✅ Encontrados {len(exact_matches)} chunks exactos para práctica {practica_num}, ordenados por relevancia")
                return [item for _, item in exact_with_sim[:top_k]]
            except Exception as e:
                print(f"Error ordenando matches exactos: {e}")
                # Si falla, devolver los primeros
                return exact_matches[:top_k]
    
    # Si no hay matches exactos o no se detectó número, usar búsqueda semántica
    # Mejorar la query para búsqueda de prácticas
    enhanced_query = query
    if practica_num:
        enhanced_query = f"práctica {practica_num} temporal feature engineering datos transaccionales " + query
    
    # Generar embedding de la consulta
    try:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=[enhanced_query]
        )
        query_embedding = response.data[0].embedding
    except Exception as e:
        print(f"Error generando embedding: {e}")
        return []
    
    # Calcular similitud con todos los chunks
    similarities = []
    for item in embeddings_data:
        similarity = cosine_similarity(query_embedding, item["embedding"])
        # Boost MUY fuerte para chunks que mencionan el número de práctica
        if practica_num:
            file_path = item["metadata"].get("file", "").lower()
            if (f"{practica_num.zfill(2)}-" in file_path or 
                f"-{practica_num}-" in file_path or
                f"{practica_num.zfill(2)}_" in file_path):
                similarity += 0.5  # Boost mucho más fuerte
        similarities.append((similarity, item))
    
    # Ordenar por similitud y tomar top_k
    similarities.sort(key=lambda x: x[0], reverse=True)
    return [item for _, item in similarities[:top_k]]

@app.route('/health', methods=['GET'])
def health():
    """Endpoint de salud."""
    return jsonify({"status": "ok", "embeddings_loaded": embeddings_data is not None})

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint principal del chatbot."""
    try:
        data = request.json
        query = data.get('query', '')
        
        if not query:
            return jsonify({"error": "Query vacía"}), 400
        
        # Buscar chunks relevantes
        relevant_chunks = search_relevant_chunks(query, top_k=5)
        
        if not relevant_chunks:
            return jsonify({
                "response": "Lo siento, no encontré información relevante en el portfolio para responder tu pregunta.",
                "sources": []
            })
        
        # Construir contexto con más información
        context_parts = []
        for i, chunk in enumerate(relevant_chunks):
            metadata = chunk['metadata']
            title = metadata.get('title', 'Sin título')
            file_path = metadata.get('file', '')
            content = chunk['content']
            
            # Extraer número de práctica si existe
            import re
            practica_match = re.search(r'(\d+)[-_]', file_path)
            practica_num = f" (Práctica {practica_match.group(1)})" if practica_match else ""
            
            context_parts.append(f"[Fuente {i+1}: {title}{practica_num}]\n{content}")
        
        context = "\n\n---\n\n".join(context_parts)
        
        # Generar respuesta con GPT
        system_prompt = """Eres un asistente inteligente que ayuda a los visitantes del portfolio de Ingeniería de Datos de la Universidad Católica del Uruguay.

INSTRUCCIONES IMPORTANTES:
1. Responde ÚNICAMENTE basándote en el contexto del portfolio proporcionado.
2. Si la pregunta menciona un número de práctica (ej: "práctica 4", "práctico 4"), busca específicamente información de esa práctica.
3. Sé preciso y específico. Si preguntan sobre una práctica en particular, enfócate en esa práctica.
4. Si no encuentras la información exacta en el contexto, di claramente que no tienes esa información específica.
5. Sé conciso pero completo. Explica de manera clara y sencilla.
6. Menciona siempre de qué práctica o sección viene la información cuando sea relevante."""
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Contexto del portfolio:\n\n{context}\n\nPregunta del usuario: {query}"}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            answer = response.choices[0].message.content
            
            # Preparar fuentes
            sources = [
                {
                    "title": chunk["metadata"]["title"],
                    "url": chunk["metadata"]["url"],
                    "file": chunk["metadata"]["file"]
                }
                for chunk in relevant_chunks
            ]
            
            return jsonify({
                "response": answer,
                "sources": sources
            })
            
        except Exception as e:
            return jsonify({"error": f"Error generando respuesta: {str(e)}"}), 500
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    load_embeddings()
    print("🚀 Servidor iniciado en http://localhost:5000")
    app.run(debug=True, port=5000)

