<center>

![./media/logo-upt.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto de Antivirus**

Curso: *Calidad y Pruebas de Software*

Docente: *Mag. Patrick Cuadros Quiroga*

Integrantes:

***LLica Mamani, Jimmy Mijair (2023076789)***

***Sierra Ruiz, Iker Alberto (2023077090)***

**Tacna – Perú**

***2026***

</center>

<div style="page-break-after: always; visibility: hidden"></div>

Sistema *SecureGuard Antivirus*

Informe de Factibilidad

Versión *1.0*

| CONTROL DE VERSIONES | | | | |
|:---:|:---|:---|:---|:---|
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | LLica Mamani, Jimmy Mijair | Sierra Ruiz, Iker Alberto | LLica Mamani, Jimmy Mijair | 28/03/2026 | Versión Original |

<div style="page-break-after: always; visibility: hidden"></div>

# **INDICE GENERAL**

[1. Descripción del Proyecto](#1-descripción-del-proyecto)

[2. Riesgos](#2-riesgos)

[3. Análisis de la Situación actual](#3-análisis-de-la-situación-actual)

[4. Estudio de Factibilidad](#4-estudio-de-factibilidad)

&nbsp;&nbsp;[4.1 Factibilidad Técnica](#41-factibilidad-técnica)

&nbsp;&nbsp;[4.2 Factibilidad económica](#42-factibilidad-económica)

&nbsp;&nbsp;[4.3 Factibilidad Operativa](#43-factibilidad-operativa)

&nbsp;&nbsp;[4.4 Factibilidad Legal](#44-factibilidad-legal)

&nbsp;&nbsp;[4.5 Factibilidad Social](#45-factibilidad-social)

&nbsp;&nbsp;[4.6 Factibilidad Ambiental](#46-factibilidad-ambiental)

[5. Análisis Financiero](#5-análisis-financiero)

&nbsp;&nbsp;[5.1 Justificación de la Inversión](#51-justificación-de-la-inversión)

&nbsp;&nbsp;&nbsp;&nbsp;[5.1.1 Beneficios del Proyecto](#511-beneficios-del-proyecto)

&nbsp;&nbsp;&nbsp;&nbsp;[5.1.2 Criterios de Inversión](#512-criterios-de-inversión)

[6. Conclusiones](#6-conclusiones)

<div style="page-break-after: always; visibility: hidden"></div>

**<u>Informe de Factibilidad</u>**

## 1. Descripción del Proyecto

### 1.1. Nombre del proyecto

SecureGuard Antivirus

### 1.2. Duración del proyecto

El proyecto tendrá una duración estimada de 16 semanas, distribuidas en 5 fases conforme al cronograma establecido en los issues del proyecto:

- Fase 1: Análisis y Fundamentos (3 semanas)
- Fase 2: Diseño de Arquitectura y Calidad (3 semanas)
- Fase 3: Desarrollo de Código y Construcción (5 semanas)
- Fase 4: Pruebas Dinámicas y Verificación (3 semanas)
- Fase 5: Gestión de Calidad y Cierre (2 semanas)

### 1.3. Descripción

El proyecto SecureGuard Antivirus consiste en el desarrollo de un software de seguridad informática especializado en la detección, prevención y eliminación de malware. Este sistema permitirá proteger los equipos de los usuarios finales mediante un motor de escaneo basado en firmas, monitoreo en tiempo real del sistema de archivos y una interfaz intuitiva que facilite la interacción con el usuario.

La importancia del proyecto radica en la creciente necesidad de proteger los sistemas informáticos contra amenazas como virus, gusanos, troyanos y ransomware. El contexto actual de transformación digital hace que la seguridad informática sea un aspecto crítico tanto para usuarios domésticos como para organizaciones.

### 1.4. Objetivos

#### 1.4.1 Objetivo general

Desarrollar un software antivirus funcional que permita detectar, prevenir y eliminar amenazas informáticas mediante un motor de escaneo basado en firmas y monitoreo en tiempo real, cumpliendo con los estándares de calidad establecidos en la norma ISO/IEC 25010.

#### 1.4.2 Objetivos Específicos

| Código | Objetivo Específico | Descripción de logro |
|:------:|:--------------------|:---------------------|
| OE-01 | Implementar un motor de escaneo eficiente | Se logrará desarrollar la lógica para la lectura de archivos y comparación de patrones contra una base de datos de firmas de virus. |
| OE-02 | Diseñar e implementar una base de datos de amenazas | Se logrará crear un esquema SQL para almacenar y gestionar las firmas de virus, permitiendo su actualización y consulta eficiente. |
| OE-03 | Desarrollar un sistema de monitoreo en tiempo real | Se logrará programar servicios que detecten cambios en el sistema de archivos de forma activa, alertando al usuario ante posibles amenazas. |
| OE-04 | Construir una interfaz de usuario intuitiva | Se logrará crear una consola o ventana gráfica que permita la interacción amigable con el usuario final. |
| OE-05 | Implementar pruebas de calidad según ISO/IEC 25010 | Se logrará medir y garantizar atributos de calidad como adecuación funcional, fiabilidad y mantenibilidad. |
| OE-06 | Documentar y gestionar la configuración del proyecto | Se logrará establecer un repositorio en GitHub con la estructura adecuada y control de versiones para el trabajo colaborativo. |

<div style="page-break-after: always; visibility: hidden"></div>

## 2. Riesgos

Señale los riesgos que pudieran afectar el éxito del proyecto.

| Código | Riesgo | Descripción | Impacto | Probabilidad | Estrategia de Mitigación |
|:------:|:-------|:------------|:-------:|:------------:|:-------------------------|
| R-01 | Falsos positivos en el escaneo | El motor de escaneo podría identificar archivos legítimos como maliciosos, afectando la confianza del usuario. | Alto | Media | Implementar pruebas unitarias rigurosas (Issue #12) y curaduría manual de la base de datos de firmas (Issue #7). |
| R-02 | Alto consumo de recursos | El monitoreo en tiempo real podría consumir excesiva CPU o RAM, degradando el rendimiento del equipo. | Alto | Media | Establecer métricas de eficiencia en el modelo de calidad (Issue #6) y optimizar el código mediante benchmarking. |
| R-03 | Desviación del alcance | Incorporación de funcionalidades no planificadas que retrasen el cronograma. | Medio | Alta | Apegarse estrictamente a la visión y alcance definido (Issue #2). |
| R-04 | Fallos en la integración de módulos | Incompatibilidad entre el motor de escaneo, la base de datos y la interfaz de usuario. | Alto | Baja | Implementar pruebas de regresión (Issue #14) después de cada merge en GitHub. |
| R-05 | Retrasos en el cronograma | Estimaciones de tiempo inexactas que afecten la entrega del proyecto. | Medio | Media | Seguimiento semanal de avances y uso de metodologías ágiles para la gestión del desarrollo. |
| R-06 | Obsolescencia tecnológica | Cambios en los sistemas operativos objetivo que afecten la compatibilidad. | Medio | Baja | Mantener una arquitectura modular (Issue #5) que permita adaptaciones futuras. |

<div style="page-break-after: always; visibility: hidden"></div>

## 3. Análisis de la Situación actual

### 3.1. Planteamiento del problema

En la actualidad, los usuarios de sistemas informáticos se enfrentan a un panorama de amenazas digitales cada vez más sofisticadas. Según reportes de seguridad, el número de ataques de malware ha incrementado significativamente en los últimos años, afectando tanto a usuarios domésticos como a organizaciones empresariales.

La problemática principal radica en que muchas soluciones antivirus existentes en el mercado son de pago, lo que limita el acceso de usuarios con recursos limitados a herramientas de protección efectivas. Adicionalmente, las soluciones gratuitas disponibles suelen ofrecer funcionalidades básicas limitadas, sin monitoreo en tiempo real o actualizaciones frecuentes de firmas.

El proyecto SecureGuard Antivirus surge como una respuesta a esta necesidad, ofreciendo una solución de código abierto que permita a los usuarios proteger sus equipos sin incurrir en costos elevados, manteniendo estándares de calidad y funcionalidades competitivas como monitoreo en tiempo real y escaneo basado en firmas.

### 3.2. Consideraciones de hardware y software

| Categoría | Recurso | Especificación | Disponibilidad |
|:----------|:--------|:---------------|:---------------|
| **Hardware** | Estaciones de desarrollo | Procesador Intel Core i5 o superior, 8GB RAM, 256GB SSD | Disponible |
| | Servidor de pruebas | Máquina virtual con 4GB RAM, 50GB almacenamiento | Disponible (VirtualBox) |
| | Equipos de prueba | Equipos con Windows 10/11, Linux (Ubuntu) | Disponible |
| **Software** | Sistema Operativo | Windows 10/11, Linux (Ubuntu 20.04/22.04) | Disponible |
| | IDE | Visual Studio Code / PyCharm Community Edition | Disponible (gratuito) |
| | Lenguaje de programación | Python 3.9+ / C++ para módulos críticos | Disponible (open source) |
| | Base de Datos | SQLite (embebida) / PostgreSQL | Disponible (open source) |
| | Control de versiones | Git + GitHub | Disponible (gratuito) |
| | Gestión de proyectos | GitHub Projects / Trello | Disponible (gratuito) |
| **Infraestructura** | Red | Conexión a internet, red LAN | Disponible |
| | Dominio | No requerido para prototipo | N/A |

<div style="page-break-after: always; visibility: hidden"></div>

## 4. Estudio de Factibilidad

El estudio de factibilidad del proyecto SecureGuard Antivirus se ha realizado siguiendo las directrices establecidas en los issues de la Fase 1, específicamente el Issue #1 (Elaboración de Informe de Factibilidad). Las actividades realizadas para preparar esta evaluación incluyen:

1. Análisis de los requerimientos técnicos y funcionales (Issue #3)
2. Evaluación de recursos disponibles para el desarrollo
3. Identificación de riesgos y estrategias de mitigación
4. Estimación de costos y beneficios del proyecto
5. Análisis del impacto en las diferentes dimensiones (legal, social, ambiental)

El presente informe ha sido aprobado por el equipo de desarrollo y será presentado al docente del curso para su revisión y aprobación.

### 4.1. Factibilidad Técnica

La viabilidad técnica evalúa si el equipo cuenta con los recursos tecnológicos necesarios para desarrollar e implementar el sistema propuesto.

**Evaluación de tecnología actual:**

| Componente | Tecnología Propuesta | Evaluación |
|:-----------|:---------------------|:-----------|
| **Motor de Escaneo** | Python con librerías nativas (`os`, `hashlib`, `re`) | ✅ Factible: Python permite manipulación de archivos y cálculos de hash de manera eficiente. Para módulos críticos se puede utilizar C++ mediante extensiones. |
| **Base de Datos de Firmas** | SQLite | ✅ Factible: Base de datos ligera, embebida, no requiere servidor adicional. Ideal para aplicaciones de escritorio. |
| **Monitoreo en Tiempo Real** | `watchdog` (Python) / `inotify` (Linux) / `ReadDirectoryChangesW` (Windows) | ✅ Factible: Existen librerías multiplataforma que abstraen las APIs del sistema operativo. |
| **Interfaz de Usuario** | Tkinter / PyQt (para versión gráfica) o CLI (para versión consola) | ✅ Factible: Ambas opciones son maduras y ampliamente documentadas. |
| **Control de Versiones** | Git + GitHub | ✅ Factible: Herramientas estandarizadas en la industria. |
| **Entorno de Pruebas** | `pytest` (unitarias), entornos virtuales aislados | ✅ Factible: Herramientas gratuitas y robustas. |

**Hardware requerido:**

- Equipos de desarrollo con capacidad para ejecutar entornos virtualizados (pruebas de malware aisladas)
- Almacenamiento suficiente para la base de datos de firmas (aproximadamente 500MB iniciales)

**Conclusión Técnica:** El proyecto es técnicamente viable. El equipo cuenta con el conocimiento necesario o la capacidad de adquirirlo, y las herramientas tecnológicas seleccionadas son de acceso gratuito y ampliamente soportadas.

### 4.2. Factibilidad Económica

El propósito del estudio de viabilidad económica es determinar los beneficios económicos del proyecto en contraposición con los costos.

#### 4.2.1. Costos Generales

Costos realizados en accesorios y material de oficina necesarios para los procesos.

| Concepto | Cantidad | Costo Unitario (S/.) | Costo Total (S/.) |
|:---------|:--------:|:--------------------:|:-----------------:|
| Papel bond A4 | 1 millar | 25.00 | 25.00 |
| Lapiceros | 4 | 2.50 | 10.00 |
| Cuaderno de apuntes | 2 | 8.00 | 16.00 |
| USB 32GB | 1 | 35.00 | 35.00 |
| Impresiones | 50 | 0.50 | 25.00 |
| **Total** | | | **111.00** |

#### 4.2.2. Costos operativos durante el desarrollo

Costos necesarios para la operatividad durante el periodo de desarrollo.

| Concepto | Descripción | Costo Total (S/.) |
|:---------|:------------|:-----------------:|
| Energía eléctrica | Consumo de equipos durante 16 semanas | 120.00 |
| Internet | Conexión para trabajo colaborativo y consultas | 200.00 |
| **Total** | | **320.00** |

#### 4.2.3. Costos del ambiente

Evaluación de requerimientos técnicos para la implantación.

| Concepto | Requerimiento | Costo | Observación |
|:---------|:--------------|:-----:|:------------|
| Infraestructura de red | Red LAN existente | S/. 0 | Disponible en el entorno universitario/domiciliario |
| Acceso a Internet | Banda ancha | S/. 0 | Ya incluido en costos operativos |
| Máquinas virtuales | VirtualBox (gratuito) | S/. 0 | Software libre |
| **Total** | | **S/. 0** | |

#### 4.2.4. Costos de personal

Gastos generados por el recurso humano necesario para el desarrollo del sistema.

| Rol | Integrante | Horas estimadas | Tarifa por hora (S/.) | Costo Total (S/.) |
|:----|:-----------|:---------------:|:--------------------:|:-----------------:|
| Jefe de Proyecto / Desarrollador | LLica Mamani, Jimmy Mijair | 120 | 25.00 | 3,000.00 |
| Desarrollador / QA | Sierra Ruiz, Iker Alberto | 120 | 25.00 | 3,000.00 |
| **Total** | | | | **6,000.00** |

*Nota: Al tratarse de un proyecto académico, este costo representa el valor del trabajo realizado, aunque no implica un desembolso real por parte de la universidad o los estudiantes.*

**Organización y horario:**

| Rol | Responsabilidades | Horario semanal |
|:----|:------------------|:----------------|
| Jefe de Proyecto | Gestión del proyecto, arquitectura, motor de escaneo, integración | 8 horas |
| Desarrollador | Base de datos, interfaz, pruebas unitarias, documentación | 8 horas |
| QA (compartido) | Pruebas funcionales, pruebas de regresión, métricas de calidad | 4 horas |

#### 4.2.5. Costos totales del desarrollo del sistema

| Categoría | Costo (S/.) |
|:----------|:-----------:|
| Costos Generales | 111.00 |
| Costos Operativos | 320.00 |
| Costos de Ambiente | 0.00 |
| Costos de Personal | 6,000.00 |
| **Costo Total del Proyecto** | **6,431.00** |

**Forma de pago:** El proyecto se desarrolla en el marco académico, por lo que no se requiere inversión inicial. Los costos generales y operativos son asumidos por los integrantes del equipo.

**Conclusión Económica:** El proyecto es económicamente viable. Los costos son mínimos (principalmente personal y servicios básicos) y pueden ser asumidos por el equipo de desarrollo.

### 4.3. Factibilidad Operativa

La factibilidad operativa evalúa si los usuarios finales podrán utilizar el sistema y si la organización cuenta con la capacidad para mantenerlo.

**Beneficios operativos:**

- Protección continua mediante monitoreo en tiempo real sin intervención manual del usuario
- Interfaz intuitiva que permite realizar escaneos programados o manuales con facilidad
- Actualización de la base de datos de firmas para mantener la protección contra nuevas amenazas

**Capacidad de mantenimiento:**

- El código fuente estará disponible en GitHub, permitiendo su mantenimiento y evolución
- La arquitectura modular (Issue #5) facilita la actualización de componentes individuales
- La documentación generada en las fases del proyecto permitirá comprender el funcionamiento interno

**Interesados identificados:**

| Interesado | Rol | Expectativas |
|:-----------|:----|:-------------|
| Usuarios finales | Utilizadores del antivirus | Protección efectiva, bajo consumo de recursos, fácil uso |
| Docente del curso | Evaluador | Cumplimiento de requisitos, calidad del producto |
| Equipo de desarrollo | Creadores | Aprendizaje, entrega exitosa del proyecto |
| Futuros contribuyentes | Desarrolladores open source | Código mantenible, documentación clara |

**Conclusión Operativa:** El proyecto es operativamente viable. Los usuarios finales podrán utilizar el sistema sin necesidad de conocimientos técnicos avanzados, y el equipo de desarrollo cuenta con la capacidad para mantenerlo.

### 4.4. Factibilidad Legal

Determina si existe conflicto del proyecto con restricciones legales.

| Aspecto Legal | Evaluación |
|:--------------|:-----------|
| **Propiedad intelectual** | El software se desarrollará como código abierto. Se utilizarán licencias compatibles (MIT, GPL) para los componentes de terceros. No se infringirán derechos de autor. |
| **Protección de datos** | El antivirus procesa archivos locales del usuario. No se recopilan ni almacenan datos personales sin consentimiento. Cumple con la Ley de Protección de Datos Personales (Ley N° 29733). |
| **Regulaciones de software de seguridad** | El software no utiliza técnicas de ingeniería inversa prohibidas. Su funcionamiento se limita al escaneo y eliminación de malware en el equipo del usuario. |
| **Criptografía** | Si se implementan funciones hash (MD5, SHA) para identificación de firmas, estas son legales y de uso permitido en el Perú. |

**Conclusión Legal:** El proyecto es legalmente viable. No se identifican conflictos con las leyes y regulaciones peruanas.

### 4.5. Factibilidad Social

Evaluación de influencias y asuntos de índole social y cultural.

| Aspecto Social | Evaluación |
|:---------------|:-----------|
| **Impacto social** | El proyecto proporciona una herramienta de seguridad gratuita, beneficiando a usuarios con recursos limitados que no pueden acceder a soluciones comerciales. |
| **Código de conducta** | El equipo de desarrollo se regirá por un código de conducta que promueve la colaboración respetuosa y la inclusión. |
| **Accesibilidad** | La interfaz se diseñará considerando principios básicos de accesibilidad para usuarios con discapacidades visuales o motrices. |
| **Educación digital** | El proyecto contribuye a la formación de los estudiantes en temas de seguridad informática y calidad de software. |

**Conclusión Social:** El proyecto es socialmente viable, con un impacto positivo al ofrecer una herramienta de seguridad gratuita y contribuir a la formación profesional.

### 4.6. Factibilidad Ambiental

Evaluación del impacto y repercusión en el medio ambiente.

| Aspecto Ambiental | Evaluación |
|:------------------|:-----------|
| **Consumo energético** | El software optimizado minimizará el consumo de recursos del equipo, reduciendo indirectamente el consumo energético. |
| **Residuos electrónicos** | Al ser software, no genera residuos físicos. Su distribución digital evita el uso de materiales físicos. |
| **Ciclo de vida** | El código abierto permite extender la vida útil del software, evitando la obsolescencia programada. |
| **Infraestructura** | Se utiliza infraestructura existente, sin necesidad de nuevo hardware. |

**Conclusión Ambiental:** El proyecto es ambientalmente viable. Su naturaleza digital y su enfoque en la eficiencia contribuyen a un impacto ambiental reducido.

<div style="page-break-after: always; visibility: hidden"></div>

## 5. Análisis Financiero

### 5.1. Justificación de la Inversión

#### 5.1.1. Beneficios del Proyecto

**Beneficios Tangibles:**

| Beneficio | Descripción | Estimación Anual (S/.) |
|:----------|:------------|:----------------------:|
| Ahorro en licencias | Los usuarios no necesitan adquirir antivirus comerciales | 200 por usuario |
| Reducción de incidentes de seguridad | Menor probabilidad de infecciones que requieran soporte técnico | 500 por incidente evitado |
| Eficiencia operativa | Automatización del escaneo y monitoreo, reduciendo intervención manual | 100 por usuario |

**Beneficios Intangibles:**

- Mejora en la seguridad de la información de los usuarios
- Contribución a la comunidad de código abierto
- Desarrollo de competencias profesionales en el equipo
- Disponibilidad de una herramienta de seguridad gratuita y confiable
- Toma acertada de decisiones mediante reportes de escaneo
- Aumento en la confiabilidad de la información procesada
- Logro de ventajas competitivas en el ámbito académico

#### 5.1.2. Criterios de Inversión

Para la evaluación financiera se considera un horizonte de 3 años, con un costo de oportunidad de capital (COK) del 12% anual.

**Proyección de beneficios anuales (para 100 usuarios):**

| Año | Beneficios Estimados (S/.) | Costos de Mantenimiento (S/.) | Beneficio Neto (S/.) |
|:---:|:--------------------------:|:-----------------------------:|:--------------------:|
| 0 | 0 | 6,431 | -6,431 |
| 1 | 20,000 | 500 | 19,500 |
| 2 | 25,000 | 600 | 24,400 |
| 3 | 30,000 | 700 | 29,300 |

*Nota: Los beneficios estimados consideran ahorro en licencias y reducción de incidentes para una base de 100 usuarios.*

##### 5.1.2.1. Relación Beneficio/Costo (B/C)

Valor Presente de los Beneficios (VPB):
- Año 1: 19,500 / (1.12)¹ = 17,410.71
- Año 2: 24,400 / (1.12)² = 19,450.76
- Año 3: 29,300 / (1.12)³ = 20,851.23
- **Total VPB = 57,712.70**

Valor Presente de los Costos (VPC):
- Año 0: 6,431 / (1.12)⁰ = 6,431.00
- Año 1: 500 / (1.12)¹ = 446.43
- Año 2: 600 / (1.12)² = 478.30
- Año 3: 700 / (1.12)³ = 498.25
- **Total VPC = 7,853.98**

**Relación B/C = VPB / VPC = 57,712.70 / 7,853.98 = 7.35**

*Interpretación: B/C > 1, por lo tanto, el proyecto se acepta.*

##### 5.1.2.2. Valor Actual Neto (VAN)

VAN = -6,431 + 19,500/(1.12)¹ + 24,400/(1.12)² + 29,300/(1.12)³

VAN = -6,431 + 17,410.71 + 19,450.76 + 20,851.23

**VAN = S/. 51,281.70**

*Interpretación: VAN > 0, por lo tanto, el proyecto se acepta.*

##### 5.1.2.3. Tasa Interna de Retorno (TIR)

La TIR se calcula como la tasa que hace el VAN igual a cero:

VAN = 0 = -6,431 + 19,500/(1+TIR)¹ + 24,400/(1+TIR)² + 29,300/(1+TIR)³

Resolviendo la ecuación:

**TIR ≈ 185%**

*Interpretación: TIR (185%) > COK (12%), por lo tanto, el proyecto se acepta.*

**Resumen de Criterios de Inversión:**

| Indicador | Valor | Criterio | Decisión |
|:----------|:-----:|:---------|:---------|
| Relación B/C | 7.35 | > 1 | Aceptar |
| VAN | S/. 51,281.70 | > 0 | Aceptar |
| TIR | 185% | > COK (12%) | Aceptar |

<div style="page-break-after: always; visibility: hidden"></div>

## 6. Conclusiones

Luego de realizar el análisis exhaustivo de factibilidad en sus diferentes dimensiones, se presentan las siguientes conclusiones:

1. **Factibilidad Técnica:** El proyecto es técnicamente viable. Se cuenta con las herramientas y conocimientos necesarios para desarrollar el motor de escaneo, la base de datos de firmas, el monitoreo en tiempo real y la interfaz de usuario. Las tecnologías seleccionadas (Python, SQLite, Git) son de acceso gratuito y ampliamente soportadas.

2. **Factibilidad Económica:** El proyecto es económicamente viable. Los costos totales estimados ascienden a S/. 6,431.00, siendo mayormente costos de personal (trabajo académico). Los costos generales y operativos son mínimos y pueden ser asumidos por el equipo de desarrollo.

3. **Factibilidad Operativa:** El proyecto es operativamente viable. Los usuarios finales podrán utilizar el sistema sin dificultad gracias a una interfaz intuitiva. El equipo de desarrollo cuenta con la capacidad para mantener el sistema y la arquitectura modular facilitará futuras actualizaciones.

4. **Factibilidad Legal:** El proyecto cumple con las disposiciones legales aplicables, incluyendo la Ley de Protección de Datos Personales y las normativas de propiedad intelectual. Se utilizarán licencias de código abierto compatibles.

5. **Factibilidad Social:** El proyecto tiene un impacto social positivo al ofrecer una herramienta de seguridad gratuita, beneficiando a usuarios con recursos limitados y contribuyendo a la formación profesional de los estudiantes.

6. **Factibilidad Ambiental:** El proyecto es ambientalmente viable. Su naturaleza digital evita la generación de residuos físicos, y su enfoque en la eficiencia contribuye a un menor consumo energético.

7. **Análisis Financiero:** Los indicadores financieros (B/C = 7.35, VAN = S/. 51,281.70, TIR = 185%) demuestran que el proyecto es rentable y genera valor, incluso considerando un escenario conservador de beneficios.

**Conclusión Final:**

El proyecto **SecureGuard Antivirus** es **VIABLE y FACTIBLE** en todas sus dimensiones. Se recomienda proceder con el desarrollo siguiendo el cronograma establecido en los issues del proyecto, iniciando con la definición de la visión y alcance (Issue #2) y la especificación detallada de requerimientos (Issue #3).

---
