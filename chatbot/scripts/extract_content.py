#!/usr/bin/env python3
"""
Script para extraer contenido de todos los archivos markdown del portfolio
y prepararlo para generar embeddings.
"""

import os
import json
import re
from pathlib import Path
from typing import List, Dict

# Rutas
ROOT_DIR = Path(__file__).parent.parent.parent
DOCS_DIR = ROOT_DIR / "docs"
OUTPUT_DIR = ROOT_DIR / "chatbot" / "data"

def clean_markdown(text: str) -> str:
    """Limpia el texto markdown removiendo sintaxis innecesaria."""
    # Remover frontmatter
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)
    
    # Remover código (mantener solo el texto)
    text = re.sub(r'```[\s\S]*?```', '[Código]', text)
    text = re.sub(r'`[^`]+`', '', text)
    
    # Remover imágenes
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    
    # Remover enlaces pero mantener el texto
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remover headers pero mantener el texto
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    
    # Limpiar espacios múltiples
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    
    return text.strip()

def extract_metadata(file_path: Path) -> Dict:
    """Extrae metadata del frontmatter."""
    metadata = {
        "file": str(file_path.relative_to(DOCS_DIR)),
        "title": file_path.stem,
        "url": f"/{file_path.relative_to(DOCS_DIR).with_suffix('')}/"
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extraer frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if key == 'title':
                        metadata['title'] = value
                    elif key == 'date':
                        metadata['date'] = value
    except Exception as e:
        print(f"Error extrayendo metadata de {file_path}: {e}")
    
    return metadata

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """Divide el texto en chunks con overlap."""
    # Dividir por párrafos primero
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = []
    current_size = 0
    
    for para in paragraphs:
        para_size = len(para)
        
        if current_size + para_size > chunk_size and current_chunk:
            # Guardar chunk actual
            chunks.append('\n\n'.join(current_chunk))
            # Mantener overlap
            overlap_text = '\n\n'.join(current_chunk[-2:]) if len(current_chunk) >= 2 else current_chunk[-1]
            current_chunk = [overlap_text] if overlap_text else []
            current_size = len(overlap_text)
        
        current_chunk.append(para)
        current_size += para_size
    
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks

def extract_portfolio_content():
    """Extrae contenido de todos los archivos markdown del portfolio."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Archivos a procesar
    markdown_files = []
    
    # Portfolio principal
    portfolio_dir = DOCS_DIR / "portfolio"
    if portfolio_dir.exists():
        markdown_files.extend(portfolio_dir.glob("*.md"))
    
    # Exploraciones extra
    exploraciones_dir = DOCS_DIR / "exploraciones-extra"
    if exploraciones_dir.exists():
        markdown_files.extend(exploraciones_dir.glob("*.md"))
    
    # Páginas principales
    main_pages = ["index.md", "acerca.md", "recursos.md", "ruta-de-aprendizaje.md"]
    for page in main_pages:
        page_path = DOCS_DIR / page
        if page_path.exists():
            markdown_files.append(page_path)
    
    print(f"📄 Encontrados {len(markdown_files)} archivos markdown")
    
    all_chunks = []
    
    for file_path in markdown_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Limpiar contenido
            clean_content = clean_markdown(content)
            
            if not clean_content or len(clean_content) < 50:
                continue
            
            # Extraer metadata
            metadata = extract_metadata(file_path)
            
            # Dividir en chunks
            chunks = chunk_text(clean_content)
            
            for i, chunk in enumerate(chunks):
                all_chunks.append({
                    "id": f"{metadata['file']}_chunk_{i}",
                    "content": chunk,
                    "metadata": {
                        **metadata,
                        "chunk_index": i,
                        "total_chunks": len(chunks)
                    }
                })
            
            print(f" {file_path.name}: {len(chunks)} chunks")
            
        except Exception as e:
            print(f" Error procesando {file_path}: {e}")
    
    # Guardar chunks
    output_file = OUTPUT_DIR / "content_chunks.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)
    
    print(f"\nExtracción completada: {len(all_chunks)} chunks guardados en {output_file}")
    print(f" Estadísticas:")
    print(f"   - Archivos procesados: {len(markdown_files)}")
    print(f"   - Chunks totales: {len(all_chunks)}")
    print(f"   - Promedio de chunks por archivo: {len(all_chunks) / len(markdown_files):.1f}")
    
    return all_chunks

if __name__ == "__main__":
    extract_portfolio_content()

