import re
import os


def define_env(env):
    """
    Definir macros personalizados para MkDocs
    """

    @env.macro
    def reading_time():
        """
        Calcula automáticamente el tiempo de lectura basado en el contenido del archivo actual
        """
        # Obtener el archivo actual
        page = env.variables.get('page')
        if not page:
            return ""

        # Leer el contenido del archivo
        file_path = page.file.abs_src_path
        if not os.path.exists(file_path):
            return ""

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remover frontmatter YAML
            content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)

            # Remover markdown y HTML
            content = re.sub(r'[#*`_\[\](){}]', '', content)  # Markdown syntax
            content = re.sub(r'<[^>]+>', '', content)  # HTML tags
            content = re.sub(r'!\[.*?\]\(.*?\)', '', content)  # Images
            content = re.sub(r'\[.*?\]\(.*?\)', '', content)  # Links

            # Contar palabras
            words = len([word for word in content.split() if word.strip()])

            # Calcular tiempo (220 palabras por minuto promedio)
            reading_speed = 220
            minutes = max(1, round(words / reading_speed))

            # Generar HTML del badge
            return f'''
<div style="display: inline-flex; align-items: center; margin: 15px 0; padding: 8px 12px; background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); border-radius: 20px; border: 1px solid #90caf9; font-size: 0.9em; color: #1565c0;">
    <span style="margin-right: 6px;">📖</span>
    <strong>Tiempo de lectura: ~{minutes} min</strong>
    <span style="margin-left: 8px; font-size: 0.8em; opacity: 0.8;">({words:,} palabras)</span>
</div>
            '''.strip()

        except Exception as e:
            return f'<span style="color: #666; font-size: 0.8em;">📖 Tiempo de lectura: ~5 min</span>'
