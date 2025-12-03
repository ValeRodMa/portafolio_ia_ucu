# Guía Rápida: Desplegar Métricas en Producción

## ✅ Estado Actual

Los embeddings ya están generados localmente e incluyen las métricas del portfolio.

- ✅ Métricas calculadas
- ✅ Contenido extraído (603 chunks, incluyendo 9 de métricas)
- ✅ Embeddings generados
- ⏳ **Pendiente: Desplegar en Render**

## 🚀 Pasos para Desplegar en Producción

### Opción A: Despliegue Automático (Git)

1. **Hacer commit de los archivos actualizados**:
```bash
cd "/Users/valentin.rodriguez.machado/Library/CloudStorage/OneDrive-Personal/UCU/IA/Ingeniería de Datos/portafolio_ia_ucu"

git add chatbot/embeddings/embeddings.json
git add chatbot/data/content_chunks.json
git add chatbot/data/portfolio_metrics.json
git add chatbot/data/portfolio_metrics.md
git add chatbot/scripts/calculate_metrics.py
git add chatbot/scripts/update_all.py
git add chatbot/*.md

git commit -m "feat: add metrics system to chatbot - portfolio statistics"
git push
```

2. **Render detectará los cambios** y re-desplegará automáticamente
3. **Verificar** en https://portafolio-ia-ucu.onrender.com/health

### Opción B: Subida Manual (si Git está en .gitignore)

Si `embeddings.json` está en `.gitignore`, necesitas subirlo manualmente:

1. **Conectar a Render por SSH** o usar el panel web
2. **Subir archivos** directamente:
   - `chatbot/embeddings/embeddings.json`
   - `chatbot/data/content_chunks.json`
   - `chatbot/data/portfolio_metrics.json`
   - `chatbot/data/portfolio_metrics.md`

3. **Reiniciar el servicio** en Render Dashboard

## 🧪 Probar el Chatbot

Una vez desplegado, prueba con estas preguntas:

### Preguntas sobre métricas
```
¿Cuál es la entrada más larga del portfolio?
¿Cuántas gráficas hay en total?
¿Qué práctica tiene más visualizaciones?
¿Cuántas prácticas hay en el portfolio?
¿Qué datasets se utilizaron?
```

### Preguntas sobre contenido (verificar que sigue funcionando)
```
¿Qué es la práctica 11?
Explícame sobre feature engineering temporal
```

## 📊 Verificar que los Embeddings Funcionan

```bash
# Probar localmente primero
cd chatbot/backend
python app.py
```

En otra terminal:
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "¿Cuál es la entrada más larga?"}'
```

## 📝 Checklist de Despliegue

- [ ] Embeddings generados localmente (✅ Ya hecho)
- [ ] Archivos commiteados a Git
- [ ] Push a GitHub
- [ ] Render re-desplegó automáticamente
- [ ] Endpoint `/health` responde OK
- [ ] Probado con pregunta sobre métricas
- [ ] Probado con pregunta sobre contenido

## ⚠️ Importante

- **Tamaño del archivo**: `embeddings.json` es ~80-100 MB
  - Git puede rechazarlo si es muy grande
  - Considera usar Git LFS si es necesario
  
- **Variables de entorno**: Asegúrate de que `OPENAI_API_KEY` esté configurada en Render

- **Tiempo de despliegue**: ~5-10 minutos en Render

## 🔄 Actualizaciones Futuras

Cuando modifiques el portfolio:

```bash
# 1. Actualizar todo localmente
python3 chatbot/scripts/update_all.py

# 2. Commit y push
git add chatbot/embeddings/ chatbot/data/
git commit -m "update: refresh portfolio metrics and embeddings"
git push

# 3. Render re-desplegará automáticamente
```

## 🐛 Troubleshooting

### El chatbot no responde sobre métricas
- Verificar que `portfolio_metrics.md` está en `chatbot/data/`
- Verificar que hay chunks de métricas: `grep "portfolio_metrics" chatbot/data/content_chunks.json`
- Verificar que los embeddings se regeneraron después de agregar las métricas

### Error "embeddings not found"
- Verificar que `chatbot/embeddings/embeddings.json` existe en Render
- Verificar los logs en Render Dashboard

### Rate limit de OpenAI
- El script ya tiene delays entre batches
- Si falla, espera 1 minuto y vuelve a ejecutar

##

Si encuentras problemas:
1. Revisar logs en Render Dashboard
2. Verificar archivos localmente
3. Probar endpoint `/health`

---

**Última actualización**: 3 de diciembre, 2025

