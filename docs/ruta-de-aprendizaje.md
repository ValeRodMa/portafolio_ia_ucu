<style>
.cv-container {
  max-width: 800px;
  margin: 0 auto;
  background: white;
  line-height: 1.6;
  color: #333;
  box-shadow: 0 0 20px rgba(0,0,0,0.1);
}

.cv-section {
  padding: 30px 40px;
}

.section-title {
  font-size: 1.4em;
  font-weight: bold;
  color: #2c3e50;
  margin-bottom: 20px;
  padding-bottom: 8px;
  border-bottom: 2px solid #3498db;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.skill-tag {
  background: #ecf0f1;
  color: #2c3e50;
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.85em;
  border: 1px solid #bdc3c7;
}

.learning-path-container {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  border-radius: 20px;
  padding: 30px;
  margin: 20px 0;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.timeline-section {
  position: relative;
  padding-left: 40px;
}

.timeline-item {
  position: relative;
  margin-bottom: 40px;
  padding: 25px;
  background: white;
  border-radius: 15px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.08);
  border-left: 5px solid #3498db;
  transition: all 0.3s ease;
}

.timeline-item:hover {
  transform: translateX(10px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}

.timeline-item:nth-child(1) { border-left-color: #e74c3c; }
.timeline-item:nth-child(2) { border-left-color: #f39c12; }
.timeline-item:nth-child(3) { border-left-color: #27ae60; }
.timeline-item:nth-child(4) { border-left-color: #8e44ad; }
.timeline-item:nth-child(5) { border-left-color: #3498db; }
.timeline-item:nth-child(6) { border-left-color: #16a085; }

.timeline-item:before {
  content: "";
  position: absolute;
  left: -50px;
  top: 25px;
  width: 20px;
  height: 20px;
  background: linear-gradient(135deg, #3498db, #2980b9);
  border-radius: 50%;
  border: 4px solid white;
  box-shadow: 0 0 0 4px #3498db, 0 5px 15px rgba(0,0,0,0.2);
}

.timeline-item:nth-child(1):before { background: linear-gradient(135deg, #e74c3c, #c0392b); box-shadow: 0 0 0 4px #e74c3c, 0 5px 15px rgba(0,0,0,0.2); }
.timeline-item:nth-child(2):before { background: linear-gradient(135deg, #f39c12, #e67e22); box-shadow: 0 0 0 4px #f39c12, 0 5px 15px rgba(0,0,0,0.2); }
.timeline-item:nth-child(3):before { background: linear-gradient(135deg, #27ae60, #229954); box-shadow: 0 0 0 4px #27ae60, 0 5px 15px rgba(0,0,0,0.2); }
.timeline-item:nth-child(4):before { background: linear-gradient(135deg, #8e44ad, #7d3c98); box-shadow: 0 0 0 4px #8e44ad, 0 5px 15px rgba(0,0,0,0.2); }
.timeline-item:nth-child(5):before { background: linear-gradient(135deg, #3498db, #2980b9); box-shadow: 0 0 0 4px #3498db, 0 5px 15px rgba(0,0,0,0.2); }
.timeline-item:nth-child(6):before { background: linear-gradient(135deg, #16a085, #13856d); box-shadow: 0 0 0 4px #16a085, 0 5px 15px rgba(0,0,0,0.2); }

.timeline-item:after {
  content: "";
  position: absolute;
  left: -40px;
  top: 45px;
  width: 2px;
  height: calc(100% + 20px);
  background: linear-gradient(to bottom, #3498db, #bdc3c7);
}

.timeline-item:last-child:after {
  display: none;
}

.timeline-date {
  background: linear-gradient(135deg, #3498db, #2980b9);
  color: white;
  padding: 8px 16px;
  border-radius: 20px;
  font-weight: bold;
  font-size: 0.85em;
  display: inline-block;
  margin-bottom: 15px;
  box-shadow: 0 3px 10px rgba(52, 152, 219, 0.3);
}

.timeline-item:nth-child(1) .timeline-date { background: linear-gradient(135deg, #e74c3c, #c0392b); box-shadow: 0 3px 10px rgba(231, 76, 60, 0.3); }
.timeline-item:nth-child(2) .timeline-date { background: linear-gradient(135deg, #f39c12, #e67e22); box-shadow: 0 3px 10px rgba(243, 156, 18, 0.3); }
.timeline-item:nth-child(3) .timeline-date { background: linear-gradient(135deg, #27ae60, #229954); box-shadow: 0 3px 10px rgba(39, 174, 96, 0.3); }
.timeline-item:nth-child(4) .timeline-date { background: linear-gradient(135deg, #8e44ad, #7d3c98); box-shadow: 0 3px 10px rgba(142, 68, 173, 0.3); }
.timeline-item:nth-child(5) .timeline-date { background: linear-gradient(135deg, #3498db, #2980b9); box-shadow: 0 3px 10px rgba(52, 152, 219, 0.3); }
.timeline-item:nth-child(6) .timeline-date { background: linear-gradient(135deg, #16a085, #13856d); box-shadow: 0 3px 10px rgba(22, 160, 133, 0.3); }

.timeline-title {
  font-weight: bold;
  color: #2c3e50;
  margin-bottom: 10px;
  font-size: 1.2em;
  display: flex;
  align-items: center;
  gap: 10px;
}

.timeline-description {
  color: #555;
  font-size: 1em;
  line-height: 1.6;
}

.timeline-description strong {
  color: #2c3e50;
  font-weight: 600;
}

.learning-path-header {
  text-align: center;
  margin-bottom: 40px;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 15px;
  color: white;
}

.learning-path-header h3 {
  margin: 0 0 10px 0;
  font-size: 1.8em;
  font-weight: bold;
}

.learning-path-header p {
  margin: 0;
  opacity: 0.9;
  font-size: 1.1em;
}

.step-progress {
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
  gap: 10px;
}

.progress-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #bdc3c7;
  transition: all 0.3s ease;
}

.progress-dot.active {
  background: linear-gradient(135deg, #3498db, #2980b9);
  box-shadow: 0 0 10px rgba(52, 152, 219, 0.5);
}

.progress-dot.completed {
  background: linear-gradient(135deg, #27ae60, #229954);
  box-shadow: 0 0 10px rgba(39, 174, 96, 0.5);
}
</style>

<div class="cv-container">

<div class="cv-section">
  <div class="learning-path-container">
    <div class="step-progress">
      <div class="progress-dot completed"></div>
      <div class="progress-dot completed"></div>
      <div class="progress-dot completed"></div>
      <div class="progress-dot completed"></div>
      <div class="progress-dot completed"></div>
      <div class="progress-dot completed"></div>
    </div>
    
    <div class="timeline-section">
      <div class="timeline-item">
        <div class="timeline-date">PASO 1 - Agosto 2025</div>
        <div class="timeline-title">
          <span style="font-size: 1.5em;">🌱</span>
          Fundamentos de EDA
        </div>
        <div class="timeline-description">
          <strong>Dataset Iris:</strong> Primer contacto con análisis exploratorio de datos. 
          Aprendí técnicas básicas de visualización con Python y Seaborn, análisis estadístico 
          descriptivo y patrones de clasificación. <br><br>
          <strong>Portfolio Setup:</strong> Configuración profesional del entorno de desarrollo 
          con MkDocs, GitHub Pages y estructura de documentación académica.
          <div style="margin-top: 15px;">
            <span class="skill-tag">Python Básico</span>
            <span class="skill-tag">Pandas</span>
            <span class="skill-tag">Seaborn</span>
            <span class="skill-tag">GitHub</span>
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-date">PASO 2 - Septiembre 2025</div>
        <div class="timeline-title">
          <span style="font-size: 1.5em;">📊</span>
          Análisis Avanzado de Datos
        </div>
        <div class="timeline-description">
          <strong>Netflix Analysis:</strong> Análisis de tendencias globales de contenido, 
          patrones temporales y distribuciones geográficas. Aplicé técnicas avanzadas de EDA 
          y profiling automático de datos. <br><br>
          <strong>NYC Taxi Pipeline:</strong> Primer proyecto de big data trabajando con 
          3M+ registros. Implementé pipeline automatizado con Prefect para orquestación 
          de workflows y análisis empresarial.
          <div style="margin-top: 15px;">
            <span class="skill-tag">Big Data</span>
            <span class="skill-tag">Prefect</span>
            <span class="skill-tag">Data Profiling</span>
            <span class="skill-tag">Workflow Orchestration</span>
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-date">PASO 3 - Octubre 2025</div>
        <div class="timeline-title">
          <span style="font-size: 1.5em;">⚖️</span>
          Calidad de Datos y Ética
        </div>
        <div class="timeline-description">
          <strong>Missing Data Detective:</strong> Análisis forense de datos faltantes 
          aplicando técnicas de imputación y consideraciones éticas sobre sesgos en 
          datasets históricos. <br><br>
          <strong>Anti-leakage Pipeline:</strong> Implementé técnicas avanzadas de prevención 
          de data leakage con validación cruzada y pipelines robustos. <br><br>
          <strong>Bias Detection:</strong> Primer contacto con ética en ML aplicando 
          framework Fairlearn para detección y corrección de sesgos algorítmicos.
          <div style="margin-top: 15px;">
            <span class="skill-tag">Data Quality</span>
            <span class="skill-tag">Data Leakage</span>
            <span class="skill-tag">Fairlearn</span>
            <span class="skill-tag">Ethics in ML</span>
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-date">PASO 4 - Noviembre 2025</div>
        <div class="timeline-title">
          <span style="font-size: 1.5em;">🔧</span>
          Feature Engineering Avanzado
        </div>
        <div class="timeline-description">
          <strong>Feature Importance Analysis:</strong> Comparación metodológica entre 
          Mutual Information y Random Forest para selección de variables en datasets 
          desbalanceados con aplicación de SMOTE. <br><br>
          <strong>Target Encoding:</strong> Técnicas avanzadas para manejo de variables 
          categóricas de alta cardinalidad, comparando Label, One-Hot, Target Encoding 
          y técnicas especializadas.
          <div style="margin-top: 15px;">
            <span class="skill-tag">Feature Selection</span>
            <span class="skill-tag">Mutual Information</span>
            <span class="skill-tag">Target Encoding</span>
            <span class="skill-tag">High Cardinality</span>
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-date">PASO 5 - Noviembre 2025</div>
        <div class="timeline-title">
          <span style="font-size: 1.5em;">🗺️</span>
          Datos Especiales: Geoespacial & Visión
        </div>
        <div class="timeline-description">
          <strong>Geoanálisis urbano (CABA):</strong> Pipeline geoespacial end-to-end con GeoPandas, 
          normalización de CRS, joins y agregaciones zonales, construcción de indicadores per cápita y hexgrids H3. <br><br>
          <strong>Preprocesamiento de imágenes:</strong> Pipeline de visión por computadora con OpenCV/scikit-image: histogramas, CLAHE, filtros bilaterales, ORB/SIFT y métricas de QA automatizadas.
          <div style="margin-top: 15px;">
            <span class="skill-tag">GeoPandas</span>
            <span class="skill-tag">H3 Hexgrids</span>
            <span class="skill-tag">OpenCV</span>
            <span class="skill-tag">scikit-image</span>
            <span class="skill-tag">Computer Vision QA</span>
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-date">PASO 6 - Exploraciones Adicionales</div>
        <div class="timeline-title">
          <span style="font-size: 1.5em;">🚀</span>
          Proyectos de Especialización
        </div>
        <div class="timeline-description">
          <strong>Wine Quality Analysis:</strong> Análisis de variables fisicoquímicas 
          que influyen en la calidad del vino aplicando técnicas de EDA avanzada. <br><br>
          <strong>Credit Card Fraud Detection:</strong> Trabajo con dataset extremadamente 
          desbalanceado (0.172% de fraude) aplicando técnicas de oversampling y análisis 
          de importancia de features. <br><br>
          <strong>Heart Disease Analysis:</strong> Replicación de técnicas de feature 
          scaling con datos médicos reales y experimentos de data leakage.
          <div style="margin-top: 15px;">
            <span class="skill-tag">SMOTE</span>
            <span class="skill-tag">Class Imbalance</span>
            <span class="skill-tag">Feature Scaling</span>
            <span class="skill-tag">Medical Data</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</div>