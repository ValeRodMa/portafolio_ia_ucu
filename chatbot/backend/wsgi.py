#!/usr/bin/env python3
"""
WSGI entry point para producción (Render, Railway, etc.)
"""
from app import app, load_embeddings

# Cargar embeddings al iniciar el servidor
load_embeddings()

if __name__ == "__main__":
    app.run()

