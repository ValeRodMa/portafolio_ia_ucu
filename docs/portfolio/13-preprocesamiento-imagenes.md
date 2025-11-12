# Preprocesamiento avanzado de imágenes: contraste, suavizado y features locales
{{ reading_time() }}
---
- **Autores**: Joaquín Batista, Milagros Cancela, Valentín Rodríguez, Alexia Aurrecoechea, Nahuel López (G1)
- **Unidad Temática**: UT4: Datos Especiales
- **Tipo**: Práctica Guiada - Assignment UT4-13
- **Entorno**: Python + OpenCV + scikit-image + NumPy + Matplotlib + Pandas
- **Dataset**: Pack clásico de `skimage` (camera, astronaut, coffee, coins, checkerboard, rocket, page)

---

**Acceso al notebook completo:** [Práctica 13 - Preprocesamiento de Imágenes](../assets/Practico_13.ipynb)

---

## 📸 Representación y diagnóstico inicial

La primera etapa consiste en leer cada imagen en color (BGR), generar variantes RGB/grises y calcular estadísticas básicas. Esto permite detectar problemas de iluminación o rangos saturados antes de aplicar transformaciones costosas.

```python
img_bgr = cv2.imread(str(img_path), cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
height, width = img_gray.shape
min_val, max_val = img_gray.min(), img_gray.max()
print(f"H={height} W={width} rango={min_val}-{max_val} μ={img_gray.mean():.2f}")
```

Hallazgos clave:

- El rango dinámico de `camera.png` cubre **0-255**, con media 115.41 → rango completo aprovechado, sin clipping.
- El histograma en grises es bimodal y se extiende en todo el espectro → **alto contraste** natural.
- En RGB el canal **R** es dominante, lo que explica el tono cálido; la implicancia es que cualquier ajuste de color debe preservar dicho balance para no introducir artefactos.

![Diagnóstico inicial: imagen y histograma](../assets/ut5_histograma_camera.png)
![Histogramas por canal (RGB)](../assets/ut5_hist_rgb.png)

### Reflexión Parte A

1. **Rango dinámico 0-255** → buena utilización tonal, la imagen contiene sombras y luces.
2. **Histograma disperso** → contraste alto; no es necesario forzar correcciones agresivas.
3. **Dominancia del canal R** → tintes cálidos; conviene cuidar la temperatura de color en procesos posteriores.

## 🎨 Espacios de color y realce de contraste

Se evaluaron dos enfoques: ecualización global en grises y CLAHE (ecualización adaptativa) sobre la luminancia `L*` en LAB. La separación del canal de luminosidad evita alterar los colores originales.

```python
img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
L, A, B = cv2.split(img_lab)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
L_clahe = clahe.apply(L)
lab_clahe = cv2.merge([L_clahe, A, B])
rgb_clahe = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2RGB)
```

Insights:

- **STD contraste**: original 75.12 → equalize 80.25 → CLAHE 75.87. La mejora global del equalize es mayor en métricas, pero CLAHE preserva detalles locales sin sobreexponer.
- El canal `L*` en LAB es el más informativo: permite ajustar luminancia sin distorsionar matices.
- CLAHE supera a la ecualización global en zonas homogéneas, ya que opera a nivel de sub-bloques y limita el ruido.

![Comparativa de contraste: original, equalize y CLAHE](../assets/ut5_contraste_comparacion.png)

### Reflexión Parte B

1. Canal más informativo: **L en LAB** (desacopla brillo y color).
2. **CLAHE** rindió mejor en áreas uniformes por la ecualización local y el límite de clip.
3. Aumento de la desviación estándar → expansión del rango tonal y mayor contraste percibido.

## 🔧 Suavizado y detección de bordes

El ruido afecta directamente a los detectores de bordes, por lo que se probaron filtros gaussiano y bilateral. Luego se aplicó Canny con umbrales constantes para comparar resultados.

```python
gaussian = cv2.GaussianBlur(img_gray, (5, 5), 0)
bilateral = cv2.bilateralFilter(img_gray, d=9, sigmaColor=75, sigmaSpace=75)
edges = cv2.Canny(bilateral, 100, 200)
```

Resultados cuantitativos:

- **Varianza del gradiente**: 10 788 → 5 335 (gauss) → 5 488 (bilateral). Ambos reducen ruido, pero el bilateral mantiene detalles.
- **Ratio de bordes**: 0.078 (original) vs 0.038 (bilateral). Menos falsos positivos tras el suavizado adaptativo.
- Recomendación: usar bilateral en escenas con aristas finas para proteger contornos.

![Suavizado y bordes (Gaussian, Bilateral, Canny)](../assets/ut5_suavizado_bordes.png)

### Reflexión Parte C

1. Filtro más efectivo: **bilateral** (balance entre reducción de ruido y preservación de bordes).
2. El ratio de bordes posterior al gaussiano sugiere **ruido residual** y bordes espurios.
3. Escenarios nocturnos → reducir umbrales de Canny a (50, 100) para capturar bordes débiles.

## ⭐ Puntos de interés y matching

Se analizó el impacto de las transformaciones sobre la densidad y repetibilidad de *keypoints* ORB.

```python
orb = cv2.ORB_create(nfeatures=1000)
kp, des = orb.detectAndCompute(variant_gray, None)
overlay = cv2.drawKeypoints(variant_gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
```

Observaciones:

- CLAHE produjo la mayor cantidad de *keypoints* válidos (~1000), ya que el realce local aumenta los gradientes.
- Repetibilidad entre original y CLAHE: **ratio 0.62**, probando que los *features* son consistentes.
- Ajustes sugeridos: `nfeatures=750`, `scaleFactor=1.1` → más cobertura con un costo moderado.

![Keypoints ORB por variante](../assets/ut5_orb_keypoints.png)
![Matching ORB: original vs CLAHE](../assets/ut5_orb_matches.png)

### Reflexión Parte D

1. Variante con mayor densidad de *keypoints*: **CLAHE** (contraste local elevado).
2. La **repetibilidad** aumentó tras CLAHE → *features* más estables entre escenas.
3. Parámetros recomendados para ORB: ajustar `nfeatures` y `scaleFactor` para equilibrar calidad/tiempo.

## 📊 Métricas de calidad y checks automáticos

Tres reglas simples facilitan la automatización del control de calidad:

- `num_keypoints < 100` → alerta crítica (escena pobre o filtrado agresivo).
- `edges_ratio ∉ [0.02, 0.15]` → bordes insuficientes o ruido excesivo.
- `STD contraste < 20` → iluminación deficiente.

Estas métricas alimentan el dashboard QA mostrado más adelante.

## 🎯 Tareas Extra (Opcional)

### 1. Curva sensibilidad vs. ruido

Se hizo un barrido de parámetros para CLAHE y filtros de suavizado. Se midió `num_keypoints` frente a un “proxy de ruido” (bordes falsos en regiones homogéneas).

```python
for clip, tile in product(clip_limits, tile_sizes):
    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=tile)
    img_proc = clahe.apply(L)
    kp, _ = orb.detectAndCompute(img_proc, None)
    noise_proxy = compute_noise_proxy(img_proc, cv2.Canny(img_proc, 100, 200))
```

Conclusión: **tile 4×4 con clipLimit 1.0** maximiza *keypoints* sin aumentar el ruido. Los suavizados gaussiano/bilateral mantienen ratios de ruido casi nulos mientras el tamaño del kernel no exceda 11.

![Curvas sensibilidad vs ruido](../assets/ut5_sensibilidad_ruido.png)

### 2. Benchmark ORB vs. SIFT

Se midió el tiempo total y los matches obtenidos por descriptor.

- ORB es ≈**3.5× más rápido** que SIFT en ambos pares evaluados.
- SIFT recupera más matches totales, pero el ratio de matches útiles es comparable (0.54 vs 0.47).
- Recomendación: ORB para pipelines en tiempo real; SIFT cuando prima la precisión y el tiempo no es crítico.

![Benchmark ORB vs SIFT](../assets/ut5_benchmark_orb_sift.png)

### 3. Dashboard QA

Se creó un tablero que muestra KPIs por imagen y resalta alertas mediante colores.

![Dashboard QA con alertas](../assets/ut5_dashboard_qa.png)

Principales hallazgos:

- 7 imágenes dispararon alertas críticas por **repetibilidad < 0.3**.
- `page.png` presentó además un `edges_ratio` fuera del rango óptimo (0.121 → advertencia).
- El tablero acelera la revisión manual, marcando en rojo/amarillo los casos problemáticos.

## 🧠 Conclusiones finales

1. **CLAHE** fue la transformación más útil para el dataset: realza detalles locales sin artefactos globales.
2. El canal **L en LAB** concentra la información de luminancia y es ideal para ajustes de contraste.
3. Existe un *trade-off* claro entre suavizado y *features*: filtros fuertes eliminan ruido pero reducen *keypoints*; debe buscarse el equilibrio en función de la tarea.
4. Checks automáticos propuestos: `num_keypoints`, `edges_ratio`, `STD` y `repeatability` garantizan detección temprana de degradaciones en el pipeline.
5. El dashboard QA permite priorizar lotes de imágenes para reprocesamiento y documentar decisiones de mantenimiento.

---

## ✅ Checklist de implementación

- [x] Diagnóstico inicial (histogramas RGB + grises)
- [x] Comparación Equalize vs CLAHE en LAB
- [x] Suavizado (Gaussian/Bilateral) + Canny con métricas de gradiente
- [x] Detección y matching de features (ORB)
- [x] Barrido de parámetros y curva sensibilidad-ruido *(opcional)*
- [x] Benchmark ORB vs SIFT *(opcional)*
- [x] Dashboard QA con alertas *(opcional)*

---

## 📚 Referencias

- OpenCV Documentation – Feature Detection (SIFT y ORB)
- scikit-image User Guide – Contrast Enhancement & Edge Detection
- Documentación oficial de ORB/SIFT y estrategias de repetibilidad en visión por computadora
