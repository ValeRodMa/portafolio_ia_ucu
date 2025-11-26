# Audio como dato: pipeline de preprocesamiento y extracción de features MFCC
{{ reading_time() }}
---
- **Autores**: Joaquín Batista, Milagros Cancela, Valentín Rodríguez, Alexia Aurrecoechea, Nahuel López (G1)
- **Unidad Temática**: UT4: Datos Especiales
- **Tipo**: Práctica Guiada - Assignment UT4-14
- **Entorno**: Python + librosa + soundfile + NumPy + Matplotlib + Pandas + scipy
- **Dataset**: UrbanSound8K (8,732 clips de audio urbano, 10 clases)

---

**Acceso al notebook completo:** [Práctica 14 - Audio como dato](../assets/Practico14.ipynb)

---

## 🎯 Objetivos de Aprendizaje

- Diseñar e implementar un pipeline completo de preprocesamiento de audio desde carga hasta exportación de features.
- Estandarizar señales de audio (sample rate, duración, amplitud) para alimentar modelos de ML.
- Analizar representaciones temporales y espectrales (waveforms, espectrogramas).
- Implementar técnicas de limpieza de ruido (filtros high-pass, recorte de silencios).
- Extraer features MFCC (Mel-Frequency Cepstral Coefficients) y métricas agregadas para clasificación.
- Evaluar el impacto de augmentación y métricas de calidad automáticas (QA).

---

## 📁 Dataset y Preparación

### UrbanSound8K

- **Fuente**: Dataset público de Kaggle (`chrisfilo/urbansound8k`).
- **Contenido**: 8,732 clips de audio urbano etiquetados en 10 clases:
  - `air_conditioner`, `car_horn`, `children_playing`, `dog_bark`, `drilling`, `engine_idling`, `gun_shot`, `jackhammer`, `siren`, `street_music`
- **Estructura**: Organizado en 10 folds para validación cruzada.
- **Formato**: Archivos WAV con sample rates variables (principalmente 48 kHz) y duraciones entre 0.5-4 segundos.

!!! note "Configuración de Kaggle API"
    Para descargar el dataset, es necesario configurar las credenciales de Kaggle API. El notebook incluye instrucciones para cargar el archivo `kaggle.json` de forma segura. Las credenciales se almacenan localmente en `~/.kaggle/kaggle.json` con permisos restringidos (600) para proteger la información sensible.

![Distribución de clips por fold](../assets/ut4_audio_folds.png)
*Distribución equilibrada de clips por fold (~800-990 por fold)*

---

## 🔧 Metodologías Aplicadas

### Parte A — Representación e inspección inicial

La primera etapa consiste en cargar un clip de ejemplo y calcular estadísticas básicas para entender la estructura de la señal.

```python
def load_audio(path: Path, sr: int | None = None, mono: bool = False):
    """Carga un archivo de audio con librosa."""
    y, sr = librosa.load(path.as_posix(), sr=sr, mono=mono)
    return y, sr

y, sr = load_audio(audio_path, sr=None, mono=False)
duration_sec = len(y) / sr if y.ndim == 1 else y.shape[-1] / sr
channels = 1 if y.ndim == 1 else y.shape[0]
```

**Hallazgos clave:**

- El audio dura aproximadamente **4.0 segundos** con sample rate **48,000 Hz**.
- La amplitud oscila entre **-0.8535 y 0.8065**, indicando que el clip está normalizado (valores dentro del rango típico [-1.0, +1.0]).
- El número de canales es **1 (mono)**, lo cual simplifica el análisis y reduce el tamaño de los datos.
- El tipo de dato (`dtype`) es `float32`, apropiado para procesamiento numérico.

**Visualización del waveform:**

![Waveform original (mono)](../assets/ut4_waveform_original.png)
*Señal temporal mostrando variaciones de amplitud a lo largo del tiempo*

### Reflexión Parte A

1. **Normalización**: Los valores están dentro del rango [-1.0, +1.0], lo que indica que la señal está correctamente normalizada y no presenta clipping.
2. **Mono vs. estéreo**: Trabajar en mono es adecuado porque la mayoría de los clips de UrbanSound8K no contienen información estéreo útil, y simplifica el análisis y reduce el tamaño de los datos.
3. **Detección de clipping**: Si observáramos muchos valores cerca de -1.0 o +1.0, esto indicaría potencialmente clipping, lo cual es problemático porque distorsiona la señal, elimina información del sonido e introduce artefactos que afectan la calidad y pueden perjudicar tareas de clasificación.

---

### Parte B — Estandarización del audio

Objetivo: unificar sample rate, mono, duración y amplitud para alimentar el pipeline de ML.

```python
TARGET_SR = 16000          # Hz
TARGET_DURATION = 3.0      # segundos
TARGET_AMPLITUDE = 0.99
TOP_DB = 30.0              # recorte de silencios

def preprocess_audio(path: Path,
                     target_sr: int = TARGET_SR,
                     target_duration: float = TARGET_DURATION,
                     top_db: float = TOP_DB) -> tuple[np.ndarray, int]:
    y, sr = load_audio(path, sr=None, mono=False)
    
    # Convertir a mono
    if y.ndim > 1:
        y = np.mean(y, axis=0)
    
    # Recortar silencios
    y_trim, _ = librosa.effects.trim(y, top_db=top_db)
    
    # Resamplear si es necesario
    if sr != target_sr:
        y_rs = librosa.resample(y_trim, orig_sr=sr, target_sr=target_sr)
    else:
        y_rs = y_trim
    
    # Ajustar duración (recortar o padear)
    target_len = int(target_sr * target_duration)
    if len(y_rs) > target_len:
        y_rs = y_rs[:target_len]
    elif len(y_rs) < target_len:
        pad_width = target_len - len(y_rs)
        y_rs = np.pad(y_rs, (0, pad_width))
    
    # Normalizar amplitud
    max_abs = np.max(np.abs(y_rs)) or 1.0
    y_norm = (TARGET_AMPLITUDE * y_rs) / max_abs
    
    return y_norm.astype(np.float32), target_sr
```

**Resultados:**

- Duración procesada: **3.0 segundos** (estandarizada).
- Amplitud procesada: min/max **-0.99 / 0.9334** (normalizada a 0.99).
- Sample rate: **16,000 Hz** (reducido desde 48 kHz para eficiencia).

![Comparativa: waveform original vs estandarizado](../assets/ut4_waveform_comparison.png)
*Efecto de la estandarización: recorte de silencios, resampleo y normalización*

### Reflexión Parte B

1. **TARGET_SR = 16000 Hz**: Elegido porque (a) es suficiente para voz y la mayoría de los sonidos urbanos (incluye frecuencias hasta ~8 kHz, adecuado para eventos del UrbanSound8K) y (b) reduce significativamente el tamaño respecto a 44.1 kHz (menos muestras, menor costo computacional, menor memoria, mayor velocidad de entrenamiento).

2. **Recorte de silencios**: El recorte con `top_db = 30` eliminó principalmente silencios muy suaves, no parte de la señal útil. El clip original mostraba largos tramos planos cerca de 0 de amplitud, exactamente los que se recortan. Los picos principales permanecen intactos en la versión estandarizada.

3. **Normalización**: Hace que el pico quede cerca de 0.99, lo cual ayuda a evitar saturación/clipping, homogeneizar la escala de todos los audios, permitir que el modelo aprenda patrones y no diferencias arbitrarias en amplitud, y mejorar estabilidad numérica en MFCC/melspectrogramas.

4. **Recorte desde inicio vs. centro**: Si recortáramos siempre el centro del clip, esto sería peor para este dataset porque UrbanSound8K contiene eventos breves y puntuales (golpes, bocinas, ladridos, sirenas). Si recortás desde el centro, corrés el riesgo de cortar la parte más importante del evento, quedarte sólo con ruido o silencio, destruir la estructura temporal del sonido. Recortar desde el inicio + trim mantiene el evento completo de forma más predecible.

---

### Parte C — Espectrogramas y ruido

#### C.1 Espectrograma de potencia

Los espectrogramas permiten visualizar la distribución de energía en el dominio frecuencia-tiempo.

```python
def plot_spectrogram(y: np.ndarray, sr: int, title: str = "") -> np.ndarray:
    n_fft = 2048
    hop_length = 512
    D = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
    librosa.display.specshow(
        S_db, sr=sr, hop_length=hop_length, x_axis="time", y_axis="hz"
    )
    return S_db
```

![Espectrograma original (mono)](../assets/ut4_spectrogram_original.png)
*Distribución espectral del audio original*

![Espectrograma estandarizado](../assets/ut4_spectrogram_standardized.png)
*Espectrograma tras estandarización (resampleo y recorte)*

#### C.2 Ruido y SNR

Se implementó la adición de ruido blanco con un SNR (Signal-to-Noise Ratio) controlado.

```python
def add_white_noise(y: np.ndarray, snr_db: float) -> np.ndarray:
    sig_power = np.mean(y**2)
    snr_linear = 10**(snr_db / 10)
    noise_power = sig_power / snr_linear
    noise = np.sqrt(noise_power) * np.random.randn(*y.shape)
    return (y + noise).astype(np.float32)
```

![Espectrograma con ruido blanco (SNR≈10 dB)](../assets/ut4_spectrogram_noisy.png)
*Ruido blanco visible como tapizado uniforme rosa/magenta en todas las frecuencias*

#### C.3 High-pass para ruido grave

Filtro Butterworth de paso alto para eliminar energía de bajas frecuencias (ruido de fondo, hum).

```python
def butter_highpass(cutoff_hz: float, sr: int, order: int = 4):
    nyq = 0.5 * sr
    norm_cutoff = cutoff_hz / nyq
    b, a = signal.butter(order, norm_cutoff, btype="high", analog=False)
    return b, a

def highpass_filter(y: np.ndarray, sr: int, cutoff_hz: float = 80.0, order: int = 4):
    b, a = butter_highpass(cutoff_hz, sr, order)
    return signal.lfilter(b, a, y)
```

![Espectrograma tras high-pass (80 Hz)](../assets/ut4_spectrogram_highpass.png)
*Eliminación de energía por debajo de 80 Hz*

### Reflexión Parte C

1. **Ruido blanco**: Se observa como magenta/rosado en el espectrograma, un tapizado uniforme en todas las frecuencias (especialmente visible en la versión con SNR=10 dB).

2. **Filtro high-pass**: Con corte en 80 Hz, (a) eliminó energía por debajo de 80 Hz y (b) afectó poco la señal útil porque la mayor parte del contenido relevante del clip se concentra por encima de ~150–2000 Hz (las componentes de los golpes/patrones rítmicos siguen intactas). El espectrograma tras el filtrado conserva claramente las mismas estructuras principales.

3. **Eliminación de hum de red**: Para eliminar hum de red usaría (a) un filtro notch en 50 o 60 Hz o (b) un high-pass con corte en 100-120 Hz. Elegiría un filtro notch porque es más específico y elimina solo la frecuencia problemática sin afectar otras componentes cercanas.

4. **Parámetros STFT**: Con `n_fft = 2048` y `hop_length = 512`, cada frame de la STFT cubre aproximadamente 128 ms. Si quisiéramos mayor resolución temporal, podríamos usar `n_fft = 512` y `hop_length = 128`, a costa de peor resolución frecuencial (bandas más gruesas), espectrograma más ruidoso, mayor costo computacional y posible pérdida de detalle tonal.

---

### Parte D — Extracción de MFCC y CSV

#### D.1 MFCC agregados

Los MFCC (Mel-Frequency Cepstral Coefficients) son features ampliamente utilizados en reconocimiento de voz y audio. Se extraen 13 coeficientes y se calculan estadísticas agregadas (media y desviación estándar).

```python
def extract_mfcc_features(y: np.ndarray, sr: int, n_mfcc: int = 13) -> dict:
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    feats = {}
    for i in range(n_mfcc):
        coef = mfcc[i, :]
        feats[f"mfcc_{i+1}_mean"] = float(np.mean(coef))
        feats[f"mfcc_{i+1}_std"] = float(np.std(coef))
    feats["rms_mean"] = float(np.mean(librosa.feature.rms(y=y)))
    feats["zcr_mean"] = float(np.mean(librosa.feature.zero_crossing_rate(y=y)))
    return feats
```

**Features generados:** 28 en total (13 MFCC × 2 estadísticas + RMS + ZCR).

#### D.2 Pipeline sobre todos los audios

Se procesaron los primeros 100 clips del dataset aplicando el pipeline completo.

```python
rows = []
for path in audio_files[:100]:
    try:
        y_proc, sr_proc = preprocess_audio(path)
        feats = extract_mfcc_features(y_proc, sr_proc)
        feats["filename"] = path.name
        feats["sr"] = sr_proc
        feats["duration_sec"] = TARGET_DURATION
        rows.append(feats)
    except Exception as exc:
        print("Error con", path.name, "→", exc)

df_features = pd.DataFrame(rows)
```

**Resultado:** DataFrame con 100 filas y 31 columnas (28 features + metadatos).

#### D.3 Guardar CSV

```python
out_csv = OUTPUTS["features"] / "audio_mfcc_features.csv"
df_features.to_csv(out_csv, index=False)
```

### Reflexión Parte D

1. **n_mfcc = 13**: Elegido porque (a) es un valor típico en voz y (b) más coeficientes agregan detalle pero también riesgo de sobreajuste por tener más dimensiones que pueden modelar ruido o variaciones irrelevantes, especialmente si el dataset no es muy grande.

2. **mfcc_1_mean captura**: (a) energía global, no (b) textura fina. El MFCC 1 (y especialmente el MFCC 0) están fuertemente correlacionados con la energía general de la señal y con su forma espectral principal. La "textura fina" (microvariaciones, armónicos, detalle de timbre) se captura más en coeficientes superiores (MFCC 5–13). Por eso, el MFCC 1_mean resume la intensidad general del sonido, no los detalles finos.

3. **Columnas adicionales para clasificación**: Para modelar clasificaciones agregarías columnas con (a) etiquetas provenientes de UrbanSound8K/metadata/UrbanSound8K.csv, específicamente la columna `classID` o `class`, y (b) alguna medida extra de ruido como SNR estimado, energía de banda baja, varianza del espectrograma, ratio señal/ruido, kurtosis o skewness del waveform, bandwidth espectral.

4. **Transformación antes de entrenar**: Antes de entrenar un modelo supervisado con estos features, convendría aplicar una transformación como `StandardScaler` / `MinMaxScaler` porque los MFCC tienen escalas muy distintas entre sí (p.ej., MFCC_1 puede estar en –400 / +100, mientras que MFCC_12 puede estar en –5 / +5). Los clasificadores y redes neuronales funcionan mejor cuando todas las features están en la misma escala, lo que mejora la estabilidad numérica, convergencia del optimizador y desempeño en SVM, kNN, redes, árboles con regularización, etc.

---

### Parte E — Exploraciones avanzadas (opcional)

#### E.1 Métricas espectrales adicionales

Se calcularon métricas dinámicas del espectro: centroid, rolloff y bandwidth.

```python
def plot_spectral_metrics(y: np.ndarray, sr: int):
    cent = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr, roll_percent=0.85)[0]
    bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
    t = librosa.times_like(cent, sr=sr)
    # ... plotting
```

![Métricas espectrales dinámicas](../assets/ut4_spectral_metrics.png)
*Evolución temporal del centroid, rolloff y bandwidth espectral*

#### E.2 Etiquetado y modelo rápido

Se extrajo el `classID` del nombre del archivo y se entrenó un modelo de clasificación rápido.

```python
def extract_classid(filename):
    parts = filename.replace(".wav", "").split("-")
    return int(parts[1])   # classID siempre en la posición 1

df_features["classID"] = df_features["filename"].apply(extract_classid)
df_features["class"] = df_features["classID"].map(class_map)

# Entrenamiento con LogisticRegression
feature_cols = [c for c in df_features.columns if "mfcc" in c or "rms" in c or "zcr" in c]
X = df_features[feature_cols]
y = df_features["classID"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = LogisticRegression(max_iter=200)
clf.fit(X_train_scaled, y_train)
print("Accuracy:", clf.score(X_test_scaled, y_test))  # 0.9
```

**Resultado:** Accuracy de **0.9** con solo 100 clips, demostrando la efectividad de los features MFCC para clasificación.

#### E.3 Augmentación básica

Se implementaron técnicas de augmentación: pitch shift y time stretch.

```python
y_pitch = librosa.effects.pitch_shift(y_std, sr=sr_std, steps=2)
y_time = librosa.effects.time_stretch(y_std, rate=0.9)
```

![Pitch shift +2 semitonos](../assets/ut4_pitch_shift.png)
*Efecto del cambio de tono en el espectrograma*

![Time stretch 0.9x](../assets/ut4_time_stretch.png)
*Efecto del estiramiento temporal en el espectrograma*

**Análisis comparativo:**

Se generaron features para versiones originales, pitch-shifted y time-stretched, y se compararon las estadísticas.

![Comparación MFCC_1_mean por versión](../assets/ut4_mfcc_augmentation.png)
*Impacto de la augmentación en los features MFCC*

**Hallazgos:**

- El pitch shift modifica principalmente los coeficientes superiores (MFCC 5-13), que capturan detalles tonales.
- El time stretch afecta la distribución temporal pero mantiene la estructura espectral general.
- La augmentación triplica el tamaño del dataset (de 100 a 300 clips), mejorando la robustez del modelo.

---

## 🎯 Tareas Extra (Opcional)

### F.1 Curva SNR → cambio en features

Se evaluó el impacto del SNR en las métricas de audio.

```python
snr_values = [0, 5, 10, 20]
rows_snr = []

for snr_db in snr_values:
    y_noisy_i = add_white_noise(y_std, snr_db=snr_db)
    feats_i = extract_mfcc_features(y_noisy_i, sr_std)
    feats_i["snr_db"] = snr_db
    rows_snr.append(feats_i)
```

![Efecto del SNR en la energía del audio](../assets/ut4_snr_rms.png)
*Relación entre SNR y energía RMS del audio*

![Efecto del SNR en la varianza del MFCC 1](../assets/ut4_snr_mfcc1_std.png)
*Impacto del ruido en la variabilidad de los features MFCC*

**Conclusión:** A medida que el SNR disminuye, la energía RMS aumenta ligeramente (el ruido añade energía), mientras que la varianza del MFCC 1 aumenta significativamente, indicando mayor inestabilidad en los features.

### F.2 Benchmark de pipelines de limpieza

Se compararon tres pipelines: raw, high-pass, y high-pass + trim.

```python
def pipeline_raw(y, sr):
    return y, "raw"

def pipeline_hp(y, sr):
    y_hp = highpass_filter(y, sr, cutoff_hz=80.0, order=4)
    return y_hp, "highpass"

def pipeline_hp_trim(y, sr):
    y_hp = highpass_filter(y, sr, cutoff_hz=80.0, order=4)
    y_trim, _ = librosa.effects.trim(y_hp, top_db=30.0)
    return y_trim, "highpass+trim"
```

**Métrica propia: Energía de bajas frecuencias (LFE)**

```python
def low_frequency_energy(y, sr, cutoff=300):
    S = np.abs(librosa.stft(y, n_fft=1024))**2
    freqs = librosa.fft_frequencies(sr=sr, n_fft=1024)
    mask = freqs < cutoff
    lfe = S[mask].sum()
    return lfe
```

![Energía de bajas frecuencias por pipeline](../assets/ut4_lfe_pipelines.png)
*Comparación de energía en bajas frecuencias (<300 Hz) entre pipelines*

**Conclusión:** El pipeline `highpass+trim` reduce significativamente la energía de bajas frecuencias, eliminando ruido de fondo y silencios, lo que mejora la calidad de los features extraídos.

### F.3 Dashboard QA de audio

Se implementó un sistema de control de calidad automático con umbrales "semáforo" (OK / Dudoso / Malo).

```python
def categorize_duration(x):
    if 2.9 <= x <= 3.1:
        return "OK"
    elif 2.5 <= x < 2.9 or 3.1 < x <= 3.5:
        return "Dudoso"
    else:
        return "Malo"

def categorize_rms(x):
    if 0.10 <= x <= 0.28:
        return "OK"
    elif 0.05 <= x < 0.10 or 0.28 < x <= 0.32:
        return "Dudoso"
    else:
        return "Malo"

def categorize_zcr(x):
    if 0.02 <= x <= 0.15:
        return "OK"
    elif 0.01 <= x < 0.02 or 0.15 < x <= 0.22:
        return "Dudoso"
    else:
        return "Malo"
```

**Resultados en 200 clips:**

- **Duración**: 200 OK (100%)
- **RMS**: 159 OK (79.5%), 23 Dudoso (11.5%), 18 Malo (9%)
- **ZCR**: 134 OK (67%), 56 Dudoso (28%), 10 Malo (5%)

![Semáforo de Duración](../assets/ut4_qa_duration.png)
*Distribución de calidad según duración*

![Semáforo de RMS](../assets/ut4_qa_rms.png)
*Distribución de calidad según energía RMS*

![Semáforo de ZCR](../assets/ut4_qa_zcr.png)
*Distribución de calidad según Zero Crossing Rate*

**Insights:**

- El 100% de los clips tienen duración correcta tras el preprocesamiento.
- El 9% de los clips tienen RMS bajo (posiblemente silencios o ruido excesivo).
- El 5% de los clips tienen ZCR fuera del rango óptimo (posiblemente ruido o señales muy suaves).

---

## 🧠 Conclusiones finales

1. **Estandarización crítica**: El estándar de entrada (sample rate = 16000 Hz, duración fija = 3.0 s, mono) es esencial porque la mayoría de los clips de UrbanSound8K no contienen información estéreo útil, y trabajar en mono reduce a la mitad el tamaño del audio, facilita la estandarización, evita duplicar información redundante y simplifica MFCC, espectrogramas y entrenamiento del modelo.

2. **Paso más efectivo**: El paso que más mejoró la calidad perceptual fue el **recorte de silencios + normalización** porque (a) redujo zonas planas, ruido de fondo débil y energía irrelevante y (b) mantuvo las partes realmente informativas del sonido (picos transitorios, patrones rítmicos y contenido espectral fuerte).

3. **Tipos de ruido detectados**: En el espectrograma detecté ruido de tipo (a) **blanco** (aparece como un tapizado uniforme rosa/magenta en todas las frecuencias), (b) **hum** (se observa energía baja sostenida en 50–60 Hz, frecuencia típica de red eléctrica), y (c) **impulsivo** (en la banda de 0–500 Hz).

4. **Checks automáticos propuestos**:
   - **SNR aproximado > 15 dB**: Garantiza que el contenido relevante es más fuerte que el ruido blanco.
   - **Duración ∈ [2.5, 3.5] s**: Permite detectar señales mal recortadas, silencios excesivos o preprocesado fallido.
   - **max(|amplitud|) ≤ 1.0**: Asegura que no haya clipping en la señal normalizada.
   - **Número de frames MFCC > 30**: Valida que el audio tenga suficiente información temporal y que no sea puro silencio o ruido.

5. **Features MFCC efectivos**: Con solo 28 features agregados (13 MFCC × 2 estadísticas + RMS + ZCR) se logró un accuracy de 0.9 en clasificación, demostrando la potencia de los MFCC para tareas de reconocimiento de audio.

6. **Augmentación valiosa**: Las técnicas de pitch shift y time stretch triplican el tamaño del dataset y mejoran la robustez del modelo sin requerir datos adicionales.

---

## ✅ Checklist de implementación

- [x] Carga y estadísticas básicas de audio
- [x] Visualización de waveform en el tiempo
- [x] Pipeline de estandarización (resampleo, recorte, padding, normalización)
- [x] Comparativa waveform original vs estandarizado
- [x] Generación de espectrogramas de potencia
- [x] Implementación de adición de ruido blanco con SNR controlado
- [x] Filtro high-pass para eliminar ruido grave
- [x] Extracción de features MFCC (13 coeficientes con estadísticas agregadas)
- [x] Pipeline completo sobre múltiples clips
- [x] Exportación a CSV de features listos para ML
- [x] Métricas espectrales adicionales (centroid, rolloff, bandwidth) *(opcional)*
- [x] Etiquetado y modelo de clasificación rápido *(opcional)*
- [x] Augmentación (pitch shift, time stretch) *(opcional)*
- [x] Curva SNR → cambio en features *(opcional)*
- [x] Benchmark de pipelines de limpieza *(opcional)*
- [x] Dashboard QA con umbrales semáforo *(opcional)*

---

## 📚 Referencias

- [librosa.load](https://librosa.org/doc/latest/generated/librosa.load.html) - Carga de archivos de audio
- [librosa.stft y espectrogramas](https://librosa.org/doc/latest/generated/librosa.stft.html) - Transformada de Fourier de tiempo corto
- [Features espectrales y MFCC en librosa](https://librosa.org/doc/latest/feature_extraction.html) - Extracción de características de audio
- [librosa.effects (pitch shift, time stretch)](https://librosa.org/doc/latest/sequence.html#module-librosa.effects) - Efectos de audio
- [scipy.signal.butter y filtros digitales](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html) - Diseño de filtros
- [API de Kaggle](https://www.kaggle.com/docs/api) - Descarga de datasets
- [kagglehub](https://github.com/Kaggle/kagglehub) - Cliente Python para Kaggle
- [Preprocesamiento en scikit-learn](https://scikit-learn.org/stable/modules/preprocessing.html) - Transformaciones de features

