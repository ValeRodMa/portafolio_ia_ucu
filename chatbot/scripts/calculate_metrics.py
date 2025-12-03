#!/usr/bin/env python3
"""
Script para calcular métricas del portfolio y generar un documento de estadísticas
que el chatbot pueda usar para responder preguntas sobre métricas.
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List
from collections import defaultdict

# Rutas
ROOT_DIR = Path(__file__).parent.parent.parent
DOCS_DIR = ROOT_DIR / "docs"
OUTPUT_DIR = ROOT_DIR / "chatbot" / "data"

def count_images(content: str) -> int:
    """Cuenta el número de imágenes en el contenido markdown."""
    # Patrón para imágenes: ![alt](url)
    image_pattern = r'!\[.*?\]\(.*?\)'
    return len(re.findall(image_pattern, content))

def count_code_blocks(content: str) -> int:
    """Cuenta el número de bloques de código."""
    # Patrón para bloques de código con ```
    code_block_pattern = r'```[\s\S]*?```'
    return len(re.findall(code_block_pattern, content))

def count_inline_code(content: str) -> int:
    """Cuenta el número de fragmentos de código inline."""
    # Patrón para código inline: `code`
    inline_code_pattern = r'`[^`]+`'
    return len(re.findall(inline_code_pattern, content))

def extract_title(file_path: Path) -> str:
    """Extrae el título del archivo markdown."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar en frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            for line in frontmatter.split('\n'):
                if line.strip().startswith('title:'):
                    title = line.split(':', 1)[1].strip().strip('"').strip("'")
                    return title
        
        # Buscar primer h1
        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            return h1_match.group(1).strip()
        
        # Usar nombre del archivo
        return file_path.stem.replace('-', ' ').title()
    except:
        return file_path.stem

def extract_datasets(content: str) -> List[str]:
    """Extrae nombres de datasets mencionados."""
    datasets = []
    common_datasets = [
        'iris', 'titanic', 'netflix', 'ames', 'boston', 'california housing',
        'wine quality', 'credit card', 'employee', 'stock', 'heart disease',
        'mnist', 'cifar'
    ]
    
    content_lower = content.lower()
    for dataset in common_datasets:
        if dataset in content_lower:
            datasets.append(dataset)
    
    return list(set(datasets))

def extract_technologies(content: str) -> List[str]:
    """Extrae tecnologías/librerías mencionadas."""
    technologies = []
    common_tech = [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 'scikit-learn', 'sklearn',
        'tensorflow', 'keras', 'pytorch', 'plotly', 'opencv', 'librosa',
        'geopandas', 'folium', 'google cloud', 'dataprep', 'fairlearn'
    ]
    
    content_lower = content.lower()
    for tech in common_tech:
        if tech in content_lower:
            technologies.append(tech)
    
    return list(set(technologies))

def count_words(content: str) -> int:
    """Cuenta palabras en el contenido (excluyendo código)."""
    # Remover bloques de código
    content = re.sub(r'```[\s\S]*?```', '', content)
    # Remover código inline
    content = re.sub(r'`[^`]+`', '', content)
    # Contar palabras
    words = content.split()
    return len(words)

def analyze_file(file_path: Path) -> Dict:
    """Analiza un archivo markdown y devuelve sus métricas."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        title = extract_title(file_path)
        
        metrics = {
            'file': str(file_path.relative_to(DOCS_DIR)),
            'title': title,
            'word_count': count_words(content),
            'char_count': len(content),
            'line_count': content.count('\n') + 1,
            'images': count_images(content),
            'code_blocks': count_code_blocks(content),
            'inline_code': count_inline_code(content),
            'datasets': extract_datasets(content),
            'technologies': extract_technologies(content),
        }
        
        return metrics
    except Exception as e:
        print(f"Error analizando {file_path}: {e}")
        return None

def calculate_portfolio_metrics():
    """Calcula todas las métricas del portfolio."""
    print("📊 Calculando métricas del portfolio...")
    
    # Recopilar archivos
    markdown_files = []
    
    # Portfolio principal
    portfolio_dir = DOCS_DIR / "portfolio"
    if portfolio_dir.exists():
        markdown_files.extend([f for f in portfolio_dir.glob("*.md") if f.name not in ['index.md', 'plantilla.md']])
    
    # Exploraciones extra
    exploraciones_dir = DOCS_DIR / "exploraciones-extra"
    if exploraciones_dir.exists():
        markdown_files.extend([f for f in exploraciones_dir.glob("*.md") if f.name != 'index.md'])
    
    print(f"📄 Analizando {len(markdown_files)} archivos...")
    
    # Analizar cada archivo
    file_metrics = []
    for file_path in markdown_files:
        metrics = analyze_file(file_path)
        if metrics:
            file_metrics.append(metrics)
            print(f"  ✓ {file_path.name}")
    
    # Calcular métricas agregadas
    total_words = sum(m['word_count'] for m in file_metrics)
    total_images = sum(m['images'] for m in file_metrics)
    total_code_blocks = sum(m['code_blocks'] for m in file_metrics)
    total_inline_code = sum(m['inline_code'] for m in file_metrics)
    
    # Encontrar entrada más larga (por palabras)
    longest_by_words = max(file_metrics, key=lambda x: x['word_count'])
    
    # Encontrar entrada con más gráficas
    most_images = max(file_metrics, key=lambda x: x['images'])
    
    # Encontrar entrada con más código
    most_code = max(file_metrics, key=lambda x: x['code_blocks'])
    
    # Recopilar todos los datasets únicos
    all_datasets = set()
    for m in file_metrics:
        all_datasets.update(m['datasets'])
    
    # Recopilar todas las tecnologías únicas
    all_technologies = set()
    for m in file_metrics:
        all_technologies.update(m['technologies'])
    
    # Contar prácticas por categoría
    portfolio_practices = [m for m in file_metrics if 'portfolio/' in m['file']]
    extra_practices = [m for m in file_metrics if 'exploraciones-extra/' in m['file']]
    
    # Crear resumen de métricas
    summary = {
        'total_entries': len(file_metrics),
        'portfolio_entries': len(portfolio_practices),
        'extra_entries': len(extra_practices),
        'total_words': total_words,
        'total_images': total_images,
        'total_code_blocks': total_code_blocks,
        'total_inline_code': total_inline_code,
        'avg_words_per_entry': total_words // len(file_metrics) if file_metrics else 0,
        'avg_images_per_entry': total_images / len(file_metrics) if file_metrics else 0,
        'longest_entry': {
            'title': longest_by_words['title'],
            'file': longest_by_words['file'],
            'word_count': longest_by_words['word_count']
        },
        'most_images_entry': {
            'title': most_images['title'],
            'file': most_images['file'],
            'image_count': most_images['images']
        },
        'most_code_entry': {
            'title': most_code['title'],
            'file': most_code['file'],
            'code_blocks': most_code['code_blocks']
        },
        'datasets_used': sorted(list(all_datasets)),
        'technologies_used': sorted(list(all_technologies)),
        'total_datasets': len(all_datasets),
        'total_technologies': len(all_technologies)
    }
    
    # Crear documento de métricas legible para humanos
    metrics_doc = generate_metrics_document(summary, file_metrics)
    
    # Guardar resultados
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Guardar JSON detallado
    metrics_file = OUTPUT_DIR / "portfolio_metrics.json"
    with open(metrics_file, 'w', encoding='utf-8') as f:
        json.dump({
            'summary': summary,
            'file_metrics': file_metrics
        }, f, ensure_ascii=False, indent=2)
    
    # Guardar documento markdown
    metrics_md_file = OUTPUT_DIR / "portfolio_metrics.md"
    with open(metrics_md_file, 'w', encoding='utf-8') as f:
        f.write(metrics_doc)
    
    print(f"\n✅ Métricas calculadas:")
    print(f"  📝 Total de entradas: {summary['total_entries']}")
    print(f"  📊 Total de palabras: {summary['total_words']:,}")
    print(f"  🖼️  Total de imágenes/gráficas: {summary['total_images']}")
    print(f"  💻 Total de bloques de código: {summary['total_code_blocks']}")
    print(f"  📈 Entrada más larga: {summary['longest_entry']['title']} ({summary['longest_entry']['word_count']:,} palabras)")
    print(f"  🎨 Entrada con más gráficas: {summary['most_images_entry']['title']} ({summary['most_images_entry']['image_count']} gráficas)")
    print(f"\n📁 Archivos generados:")
    print(f"  - {metrics_file}")
    print(f"  - {metrics_md_file}")
    
    return summary, file_metrics

def generate_metrics_document(summary: Dict, file_metrics: List[Dict]) -> str:
    """Genera un documento markdown con las métricas del portfolio."""
    doc = """# Métricas y Estadísticas del Portfolio

Este documento contiene estadísticas y métricas del portfolio de Ingeniería de Datos.

## Resumen General

"""
    
    doc += f"- **Total de entradas/prácticas**: {summary['total_entries']}\n"
    doc += f"  - Prácticas del portfolio principal: {summary['portfolio_entries']}\n"
    doc += f"  - Exploraciones extra: {summary['extra_entries']}\n"
    doc += f"- **Total de palabras**: {summary['total_words']:,}\n"
    doc += f"- **Promedio de palabras por entrada**: {summary['avg_words_per_entry']:,}\n"
    doc += f"- **Total de imágenes/gráficas**: {summary['total_images']}\n"
    doc += f"- **Promedio de gráficas por entrada**: {summary['avg_images_per_entry']:.1f}\n"
    doc += f"- **Total de bloques de código**: {summary['total_code_blocks']}\n"
    doc += f"- **Total de fragmentos de código inline**: {summary['total_inline_code']}\n"
    
    doc += "\n## Récords y Destacados\n\n"
    
    doc += f"### Entrada más larga (por contenido)\n"
    doc += f"- **Título**: {summary['longest_entry']['title']}\n"
    doc += f"- **Archivo**: {summary['longest_entry']['file']}\n"
    doc += f"- **Palabras**: {summary['longest_entry']['word_count']:,}\n"
    
    doc += f"\n### Entrada con más gráficas/imágenes\n"
    doc += f"- **Título**: {summary['most_images_entry']['title']}\n"
    doc += f"- **Archivo**: {summary['most_images_entry']['file']}\n"
    doc += f"- **Número de gráficas**: {summary['most_images_entry']['image_count']}\n"
    
    doc += f"\n### Entrada con más código\n"
    doc += f"- **Título**: {summary['most_code_entry']['title']}\n"
    doc += f"- **Archivo**: {summary['most_code_entry']['file']}\n"
    doc += f"- **Bloques de código**: {summary['most_code_entry']['code_blocks']}\n"
    
    doc += "\n## Datasets Utilizados\n\n"
    doc += f"Total de datasets diferentes: {summary['total_datasets']}\n\n"
    if summary['datasets_used']:
        for dataset in summary['datasets_used']:
            doc += f"- {dataset.title()}\n"
    
    doc += "\n## Tecnologías y Librerías\n\n"
    doc += f"Total de tecnologías utilizadas: {summary['total_technologies']}\n\n"
    if summary['technologies_used']:
        for tech in summary['technologies_used']:
            doc += f"- {tech}\n"
    
    doc += "\n## Métricas por Entrada\n\n"
    doc += "| Título | Palabras | Imágenes | Código | Datasets |\n"
    doc += "|--------|----------|----------|--------|----------|\n"
    
    # Ordenar por palabras descendente
    sorted_metrics = sorted(file_metrics, key=lambda x: x['word_count'], reverse=True)
    for m in sorted_metrics:
        datasets_str = ', '.join(m['datasets'][:3]) if m['datasets'] else '-'
        if len(m['datasets']) > 3:
            datasets_str += '...'
        doc += f"| {m['title'][:40]} | {m['word_count']:,} | {m['images']} | {m['code_blocks']} | {datasets_str} |\n"
    
    doc += "\n## Top 5 Entradas por Categoría\n\n"
    
    doc += "### Por longitud (palabras)\n"
    top_by_words = sorted(file_metrics, key=lambda x: x['word_count'], reverse=True)[:5]
    for i, m in enumerate(top_by_words, 1):
        doc += f"{i}. **{m['title']}** - {m['word_count']:,} palabras\n"
    
    doc += "\n### Por número de gráficas\n"
    top_by_images = sorted(file_metrics, key=lambda x: x['images'], reverse=True)[:5]
    for i, m in enumerate(top_by_images, 1):
        doc += f"{i}. **{m['title']}** - {m['images']} gráficas\n"
    
    doc += "\n### Por cantidad de código\n"
    top_by_code = sorted(file_metrics, key=lambda x: x['code_blocks'], reverse=True)[:5]
    for i, m in enumerate(top_by_code, 1):
        doc += f"{i}. **{m['title']}** - {m['code_blocks']} bloques de código\n"
    
    doc += "\n---\n"
    doc += "\n*Documento generado automáticamente por calculate_metrics.py*\n"
    
    return doc

if __name__ == "__main__":
    calculate_portfolio_metrics()

