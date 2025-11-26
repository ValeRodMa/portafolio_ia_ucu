---
title: "Introducción a Google Cloud: primeros pasos con la consola y servicios"
date: 2025-11-26
---

# Introducción a Google Cloud: primeros pasos con la consola y servicios
{{ reading_time() }}

---
- **Autores**: Joaquín Batista, Milagros Cancela, Valentín Rodríguez, Alexia Aurrecoechea, Nahuel López (G1)
- **Unidad Temática**: UT5: Pipelines ETL
- **Tipo**: Práctica Guiada - Google Cloud Skills Boost Lab
- **Entorno**: Google Cloud Console + Qwiklabs
- **Lab**: [A Tour of Google Cloud Hands-on Labs](https://www.skills.google/focuses/2794?catalog_rank=%7B%22rank%22%3A3%2C%22num_filters%22%3A2%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=60924676)
- **Fecha**: Noviembre 2025

---

## 🎯 Objetivos de Aprendizaje

Esta práctica introductoria proporciona una experiencia práctica con Google Cloud Platform (GCP), explorando la consola de Cloud, proyectos, IAM, roles, permisos y APIs. El lab está diseñado para familiarizarse con los conceptos fundamentales de la infraestructura en la nube y sentar las bases para construir pipelines ETL escalables.

### Objetivos Principales

- **Acceder a la Cloud Console** y explorar la interfaz de usuario de Google Cloud
- **Comprender el concepto de proyectos** y su rol como organizadores de recursos
- **Gestionar roles y permisos** usando Cloud IAM (Identity and Access Management)
- **Habilitar APIs y servicios** necesarios para diferentes funcionalidades
- **Familiarizarse con la plataforma Qwiklabs** y el entorno de labs temporales

---

## 📚 Lo que se Aprendió

### 1. **Conceptos Fundamentales de Google Cloud**

**Proyectos como Organizadores de Recursos:**
- Un proyecto de Google Cloud es una entidad organizadora que contiene recursos, servicios, configuraciones y permisos
- Cada proyecto tiene un **Project ID único** globalmente identificable (ej: `qwiklabs-gcp-xxx...`)
- Los proyectos permiten agrupar recursos relacionados (VMs, bases de datos, redes) y gestionar su acceso de forma centralizada
- Los proyectos también contienen configuraciones de facturación y seguridad

**Cloud Console como Hub Central:**
- La Cloud Console es la interfaz web principal para acceder y gestionar todos los servicios de Google Cloud
- Proporciona acceso a más de 200+ servicios y APIs desde una interfaz unificada
- Permite visualizar recursos, monitorear uso, gestionar permisos y configurar servicios sin necesidad de línea de comandos

### 2. **Identity and Access Management (IAM)**

**Roles Básicos:**
- **`roles/viewer`**: Permisos de solo lectura, no afectan el estado de los recursos
- **`roles/editor`**: Todos los permisos de viewer + capacidad de modificar recursos existentes
- **`roles/owner`**: Todos los permisos de editor + gestión de roles, permisos y configuración de facturación

**Principios de IAM:**
- Los roles básicos establecen permisos a nivel de proyecto
- A menos que se especifique lo contrario, controlan el acceso a todos los servicios de Google Cloud
- Los permisos son temporales en el entorno de labs (solo durante la duración del lab)
- La gestión de acceso es fundamental para la seguridad en la nube

**Práctica con IAM:**
- Se aprendió a otorgar roles a diferentes identidades (principals)
- Se experimentó con la interfaz de "Grant access" para asignar roles específicos
- Se verificó la asignación correcta de roles en la página de IAM

### 3. **APIs y Servicios de Google Cloud**

**Biblioteca de APIs:**
- Google Cloud ofrece más de 200+ APIs que cubren áreas desde administración de negocios hasta machine learning
- Las APIs siguen principios de diseño orientado a recursos (resource-oriented design)
- Cada API proporciona información detallada sobre uso, niveles de tráfico, tasas de error y latencias

**Habilitación de APIs:**
- En labs, muchas APIs se habilitan automáticamente para facilitar el trabajo
- En proyectos propios, es necesario habilitar APIs manualmente según las necesidades
- El proceso de habilitación es simple: navegar a APIs & Services > Library > buscar API > Enable

**Ejemplo Práctico - Dialogflow API:**
- Se exploró la API de Dialogflow para construir aplicaciones conversacionales
- Se habilitó la API y se exploró la documentación disponible
- Se comprendió cómo las APIs permiten integrar servicios de Google Cloud en aplicaciones

### 4. **Plataforma Qwiklabs y Entorno de Labs**

**Características del Entorno:**
- Los labs crean un entorno temporal de Google Cloud con servicios y credenciales habilitados
- Cada lab tiene un tiempo límite (countdown timer) que determina la duración del acceso
- Las credenciales son temporales y específicas del lab (`student-xx-xxxxxx@qwiklabs.net`)
- Al finalizar el tiempo, el entorno y recursos se eliminan automáticamente

**Activity Tracking:**
- Muchos labs incluyen un sistema de puntuación que verifica la finalización de pasos específicos
- Para pasar un lab con activity tracking, es necesario completar todos los pasos en orden
- El scoring contribuye a badges, credenciales y posiciones en leaderboards

---

## 🚧 Lo que Más Costó

### 1. **Gestión de Credenciales y Sesiones**

**Desafío:**
- La necesidad de usar credenciales temporales específicas del lab (`student-xx-xxxxxx@qwiklabs.net`)
- Confusión potencial al mezclar credenciales personales/corporativas con las del lab
- El riesgo de cerrar sesión accidentalmente si se usa la cuenta personal en el mismo navegador

**Solución Aprendida:**
- Usar ventanas de navegación privada (Incognito/Private) para evitar conflictos
- Asegurarse de hacer clic en "Use Another Account" cuando aparece la página de selección de cuenta
- Verificar siempre que se está usando la cuenta del lab, no la personal

### 2. **Comprensión de Roles y Permisos**

**Desafío:**
- Entender las diferencias sutiles entre los roles básicos (viewer, editor, owner)
- Comprender qué acciones están permitidas con cada rol
- Determinar qué rol asignar en diferentes escenarios

**Solución Aprendida:**
- Revisar la documentación de roles para entender permisos específicos
- Practicar otorgando diferentes roles y verificando qué acciones son posibles
- Comprender que los roles básicos son amplios y que existen roles más granulares disponibles

### 3. **Navegación en la Cloud Console**

**Desafío:**
- La Cloud Console tiene muchos menús y opciones que pueden ser abrumadores inicialmente
- Encontrar servicios específicos entre la gran cantidad de opciones disponibles
- Entender la organización jerárquica de servicios y recursos

**Solución Aprendida:**
- Usar el menú de navegación (hamburger menu) para explorar categorías de servicios
- Utilizar la barra de búsqueda para encontrar servicios específicos rápidamente
- Familiarizarse con las secciones principales: Compute, Storage, Big Data, Networking, etc.

### 4. **Gestión del Tiempo en Labs**

**Desafío:**
- Los labs tienen tiempo limitado y no se pueden pausar
- El riesgo de perder trabajo si el tiempo se agota antes de completar todas las tareas
- La necesidad de trabajar eficientemente sin perder tiempo en pasos innecesarios

**Solución Aprendida:**
- Leer las instrucciones completas antes de comenzar el lab
- Trabajar de forma organizada y seguir los pasos en orden
- No hacer clic en "End Lab" hasta completar todas las tareas
- Mantener ambas pestañas abiertas (instrucciones y Cloud Console) para referencia rápida

---

## ✨ Lo Nuevo que se Descubrió

### 1. **Modelo de Precios Basado en Uso**

**Descubrimiento:**
- Google Cloud utiliza un modelo de precios basado en el consumo real de recursos
- Servicios como BigQuery cobran según el volumen de datos procesados por consulta
- Esto enfatiza la importancia de escribir consultas eficientes para minimizar costos
- El modelo "pay-as-you-go" permite escalar según necesidades sin compromisos a largo plazo

**Implicaciones:**
- La optimización de consultas y recursos no solo mejora el rendimiento, sino que también reduce costos
- Es crucial monitorear el uso de recursos para evitar cargos inesperados
- Los labs proporcionan créditos temporales, pero en proyectos reales es importante gestionar el presupuesto

### 2. **Integración con Herramientas de Visualización**

**Descubrimiento:**
- Google Cloud se integra nativamente con herramientas de visualización como Data Studio
- Los datos almacenados en BigQuery y Cloud SQL pueden conectarse directamente a dashboards
- Esta integración facilita la creación de informes interactivos sin necesidad de exportar datos manualmente

**Aplicaciones:**
- Crear dashboards en tiempo real basados en datos de Google Cloud
- Compartir visualizaciones con stakeholders sin acceso técnico a la consola
- Automatizar la generación de reportes basados en datos actualizados

### 3. **Activity Tracking y Gamificación**

**Descubrimiento:**
- El sistema de activity tracking en Qwiklabs verifica automáticamente la finalización de tareas
- Los labs pueden incluir checkpoints que validan el progreso antes de continuar
- El sistema de badges y credenciales motiva el aprendizaje continuo

**Beneficios:**
- Validación automática de conocimientos adquiridos
- Retroalimentación inmediata sobre el progreso
- Sistema de logros que incentiva completar más labs y profundizar en temas específicos

### 4. **Arquitectura de Recursos Orientada a Recursos**

**Descubrimiento:**
- Las APIs de Google Cloud siguen principios de diseño orientado a recursos (RESTful)
- Cada recurso tiene un identificador único y puede ser manipulado mediante operaciones estándar
- Esta arquitectura facilita la integración y automatización mediante código

**Ventajas:**
- Consistencia en cómo se interactúa con diferentes servicios
- Facilita la automatización mediante scripts y herramientas de CI/CD
- Permite construir pipelines complejos que integran múltiples servicios

---

## 💡 Algo Más Interesante

### 1. **Escalabilidad y Elasticidad de la Nube**

Una de las características más impresionantes de Google Cloud es su capacidad de escalar recursos automáticamente según la demanda. A diferencia de infraestructura tradicional donde se necesita comprar hardware físico, en la nube puedes:

- **Escalar horizontalmente**: Agregar más instancias de un servicio cuando aumenta la carga
- **Escalar verticalmente**: Aumentar la capacidad de recursos existentes (CPU, RAM, almacenamiento)
- **Auto-scaling**: Configurar políticas para que el sistema escale automáticamente según métricas predefinidas

Esto es especialmente relevante para pipelines ETL que pueden tener cargas variables. Por ejemplo, un pipeline que procesa datos diariamente puede escalar durante las horas pico y reducirse durante períodos de baja actividad, optimizando costos.

### 2. **Seguridad Multi-Capa**

Google Cloud implementa seguridad en múltiples capas:

- **Seguridad de red**: Firewalls, VPCs (Virtual Private Clouds), y reglas de acceso
- **Seguridad de identidad**: IAM con roles granulares y políticas de acceso
- **Seguridad de datos**: Encriptación en tránsito y en reposo
- **Cumplimiento**: Certificaciones ISO, SOC, HIPAA, etc.

Lo interesante es cómo estas capas trabajan juntas. Por ejemplo, incluso si alguien obtiene acceso a un recurso, las políticas de IAM pueden prevenir acciones no autorizadas, y el logging de Cloud Audit Logs registra todas las acciones para auditoría.

### 3. **Ecosistema Integrado**

Google Cloud no es solo una colección de servicios independientes, sino un ecosistema integrado donde los servicios trabajan juntos sin problemas:

- **BigQuery** puede leer directamente de **Cloud Storage**
- **Dataflow** puede procesar datos y escribir resultados en **BigQuery**
- **Cloud Functions** puede activarse por eventos de **Pub/Sub** o cambios en **Cloud Storage**
- **Cloud Composer** (Apache Airflow) puede orquestar pipelines complejos usando múltiples servicios

Esta integración facilita enormemente la construcción de pipelines ETL complejos sin necesidad de configurar conexiones manuales entre servicios.

### 4. **Observabilidad y Monitoreo**

Google Cloud proporciona herramientas poderosas para monitorear y entender el comportamiento de los sistemas:

- **Cloud Monitoring**: Métricas, alertas y dashboards personalizados
- **Cloud Logging**: Agregación centralizada de logs de todos los servicios
- **Cloud Trace**: Trazado distribuido para entender el flujo de requests a través de servicios
- **Cloud Profiler**: Análisis de rendimiento de aplicaciones

Lo interesante es cómo estas herramientas ayudan a identificar cuellos de botella, optimizar costos y mejorar la confiabilidad de los pipelines ETL. Por ejemplo, puedes identificar qué consultas de BigQuery son más costosas y optimizarlas, o detectar patrones de error en logs para mejorar la robustez del pipeline.

### 5. **Aprendizaje Continuo y Comunidad**

La plataforma Google Cloud Skills Boost (anteriormente Qwiklabs) ofrece:

- **700+ labs y cursos** cubriendo desde conceptos básicos hasta temas avanzados
- **Learning paths** estructurados para diferentes roles (Data Engineer, ML Engineer, etc.)
- **Badges y certificaciones** que validan conocimientos
- **Comunidad activa** de aprendices y expertos

Lo interesante es cómo esta plataforma facilita el aprendizaje práctico. En lugar de solo leer documentación, puedes experimentar con servicios reales en un entorno seguro y temporal, lo cual acelera significativamente la curva de aprendizaje.

---

## 🎓 Reflexiones Finales

Esta práctica introductoria proporcionó una base sólida para trabajar con Google Cloud. Los conceptos aprendidos sobre proyectos, IAM, y APIs son fundamentales para cualquier trabajo posterior con pipelines ETL en la plataforma.

**Próximos Pasos:**
- Explorar servicios específicos de ETL como Cloud Dataflow, Cloud Dataprep, y BigQuery
- Aprender a construir pipelines automatizados usando Cloud Composer
- Experimentar con integración de datos entre diferentes servicios de Google Cloud

**Aplicaciones Prácticas:**
- Los conocimientos de IAM serán esenciales para gestionar acceso en proyectos de equipo
- La comprensión de proyectos ayudará a organizar recursos de forma lógica
- El conocimiento de APIs facilitará la automatización de tareas mediante código

---

## 📚 Recursos Adicionales

- [Google Cloud Documentation](https://cloud.google.com/docs)
- [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)
- [IAM Best Practices](https://cloud.google.com/iam/docs/using-iam-securely)
- [Google Cloud APIs Explorer](https://developers.google.com/apis-explorer)

---

> 💡 **Nota**: Esta práctica fue realizada en el entorno temporal de Qwiklabs. Para proyectos reales, es importante considerar aspectos de seguridad, costos y mejores prácticas de arquitectura en la nube.

