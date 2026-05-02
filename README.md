# 🛡️ SecureGuard Antivirus

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Rust](https://img.shields.io/badge/Engine-Rust%201.75%2B-orange.svg)](https://www.rust-lang.org/)
[![Python](https://img.shields.io/badge/GUI-Python%203.10%2B-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11-lightgrey.svg)]()
[![Version](https://img.shields.io/badge/Version-v1.0-green.svg)](releases)

> **SecureGuard Antivirus** es una solución de seguridad informática de código abierto que detecta, previene y elimina malware mediante un motor de escaneo basado en firmas SHA-256, análisis heurístico de entropía y monitoreo en tiempo real del sistema de archivos. Desarrollado como proyecto académico en la Universidad Privada de Tacna.

---

## 📋 Descripción

SecureGuard Antivirus combina un **motor de alto rendimiento escrito en Rust** con una **interfaz gráfica moderna en Python (CustomTkinter)**, comunicándose mediante un protocolo JSON sobre IPC. Ofrece las funcionalidades esenciales de un antivirus de escritorio: escaneo bajo demanda, protección en tiempo real, cuarentena, control de firewall, limpieza del sistema y actualización de firmas desde repositorio.

### ✨ Características Principales

| Módulo | Descripción |
|:-------|:------------|
| 🔍 **Motor de Escaneo** | Detección por hash SHA-256, heurística de entropía y strings sospechosos |
| 🛡️ **Protección en Tiempo Real** | Monitoreo de Documentos, Descargas y carpetas del sistema con `notify` |
| 🔒 **Cuarentena** | Aislamiento, restauración y eliminación de archivos amenazantes |
| 🌐 **Control de Firewall** | Activar/desactivar Windows Firewall desde la GUI |
| 🧹 **Limpieza del Sistema** | Eliminación de archivos temporales de Windows |
| 🔄 **Actualización de Firmas** | Descarga de hashes SHA-256 y reglas YARA desde repositorio |
| 📊 **Dashboard** | Indicador de estado en tiempo real con alertas visuales |

---

## 🛠️ Tecnologías Utilizadas

### Backend — Motor de Seguridad
- **Lenguaje:** [Rust](https://www.rust-lang.org/) 1.75+
- **Crates principales:** `serde_json`, `walkdir`, `sha2`, `notify`, `reqwest`, `dirs`
- **Compilado a:** `secureguard_engine.exe` (ejecutable nativo Windows)

### Frontend — Interfaz Gráfica
- **Lenguaje:** [Python](https://python.org) 3.10+
- **Framework GUI:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) 5.2.0
- **Dependencias:** `psutil`, `Pillow`, `plyer`, `requests`
- **Empaquetado:** [PyInstaller](https://pyinstaller.org/)

### Comunicación
- **IPC:** JSON línea-a-línea sobre `stdin`/`stdout` del subproceso motor

---

## ⚙️ Requisitos Previos

### Para ejecutar desde código fuente:

- **Sistema Operativo:** Windows 10 / Windows 11 (64-bit)
- **Python:** 3.10 o superior ([descargar](https://python.org/downloads))
- **Rust toolchain:** 1.75 o superior ([descargar](https://rustup.rs/)) — *solo para compilar el motor*
- **RAM:** 4 GB mínimo
- **Disco:** 500 MB libres
- **Permisos:** Administrador (requerido para control de firewall y cuarentena)

### Para usar el instalador precompilado:
- Windows 10/11 (64-bit)
- Permisos de administrador

---

## 🚀 Instalación Paso a Paso

### Opción A — Instalador precompilado (recomendado)

```bash
# 1. Navegar a la carpeta del instalador
cd codigo-fuente/Instalador/BitCraft_Antivirus/

# 2. Ejecutar como administrador
BitCraft_Antivirus.exe
```

### Opción B — Desde código fuente

#### 1. Clonar el repositorio

```bash
git clone https://github.com/IkerASierraR/proyecto_antivirus.git
cd proyecto_antivirus
```

#### 2. Compilar el motor Rust

```bash
cd codigo-fuente/backend_rust

# Compilar en modo release (optimizado)
cargo build --release

# El ejecutable queda en:
# target/release/secureguard_engine.exe
```

#### 3. Instalar dependencias Python

```bash
cd ../frontend_python
pip install -r requirements.txt
```

#### 4. Configurar el motor

```bash
# Crear directorio de firmas
mkdir signatures

# (Opcional) Agregar hashes iniciales al archivo de firmas
# Cada línea debe contener un hash SHA-256
echo "# SecureGuard Malware Hashes" > signatures/malware_hashes.txt
```

#### 5. Colocar el motor compilado

```bash
# Copiar el ejecutable compilado al directorio frontend
copy ..\backend_rust\target\release\secureguard_engine.exe .
```

---

## ▶️ Ejecución del Sistema

### Ejecución completa (GUI + Motor)

```bash
# Desde el directorio frontend_python/
python main.py
```

La aplicación inicia automáticamente el motor en modo daemon y muestra la interfaz gráfica.

### Ejecución solo del motor (modo CLI)

```bash
# Escanear un directorio
secureguard_engine.exe scan "C:\Users\Public"

# Limpiar archivos temporales
secureguard_engine.exe clean

# Actualizar firmas
secureguard_engine.exe update

# Activar firewall
secureguard_engine.exe firewall_on

# Modo daemon (acepta comandos JSON por stdin)
secureguard_engine.exe daemon "C:\ruta\signatures"
```

---

## 📡 Parámetros del Motor

| Comando | Argumento | Descripción |
|:--------|:----------|:------------|
| `daemon` | `<ruta_signatures>` | Iniciar motor en modo persistente (lee JSON de stdin) |
| `scan` | `<ruta_directorio>` | Escanear directorio y retornar resultados JSON |
| `clean` | — | Limpiar archivos temporales de Windows |
| `update` | — | Actualizar firmas desde repositorio remoto |
| `firewall_on` | — | Activar Windows Firewall (requiere administrador) |
| `firewall_off` | — | Desactivar Windows Firewall (requiere administrador) |

### Protocolo de comandos (modo daemon)

```json
// Escanear directorio
{"action": "scan", "path": "C:\\Users\\Public"}

// Activar protección en tiempo real
{"action": "start_realtime"}

// Listar archivos en cuarentena
{"action": "list_quarantine"}

// Restaurar archivo de cuarentena
{"action": "restore_quarantine", "file": "<sha256>.quar"}

// Eliminar archivo de cuarentena
{"action": "delete_quarantine", "file": "<sha256>.quar"}

// Activar/desactivar firewall
{"action": "firewall_on"}
{"action": "firewall_off"}

// Limpiar archivos temporales
{"action": "clean"}

// Actualizar firmas
{"action": "update"}
```

---

## 💡 Ejemplo de Uso

### Escaneo desde la GUI

1. Abrir SecureGuard Antivirus
2. En el **Dashboard**, hacer clic en **"🔍 Escanear Equipo (Rápido)"**
3. Esperar a que la barra de progreso complete el escaneo
4. El indicador de estado mostrará el resultado:
   - 🟢 **Verde:** Sistema protegido, sin amenazas
   - 🔴 **Rojo:** Amenaza detectada (archivo movido a cuarentena automáticamente)

### Activar protección en tiempo real

1. Navegar a **"🛡️ Protección"** en el sidebar
2. Activar el switch **"Protección en Tiempo Real"**
3. El motor comenzará a monitorear Documentos, Descargas y carpetas públicas

### Ver y gestionar cuarentena

1. Navegar a **"🔒 Cuarentena"** en el sidebar
2. Hacer clic en **"Actualizar lista"** para ver archivos aislados
3. Seleccionar un archivo y usar **"Restaurar"** o **"Eliminar"** según corresponda

---

## 📁 Estructura del Proyecto

```
proyecto_antivirus/
├── 📂 codigo-fuente/
│   ├── 📂 backend_rust/          # Motor de seguridad en Rust
│   │   ├── src/
│   │   │   ├── main.rs           # Punto de entrada + dispatcher CLI
│   │   │   ├── scanner.rs        # Motor de escaneo (hash + heurística)
│   │   │   ├── daemon.rs         # Manejador de comandos JSON
│   │   │   ├── quarantine.rs     # Gestión de cuarentena
│   │   │   ├── network.rs        # Control del firewall de Windows
│   │   │   ├── cleaner.rs        # Limpieza de archivos temporales
│   │   │   ├── updater.rs        # Actualización de firmas
│   │   │   ├── protection.rs     # Monitoreo en tiempo real
│   │   │   └── utils.rs          # Helpers de respuestas JSON
│   │   ├── Cargo.toml
│   │   └── Cargo.lock
│   │
│   ├── 📂 frontend_python/       # Interfaz gráfica en Python
│   │   ├── views/
│   │   │   ├── dashboard_view.py
│   │   │   ├── protection_view.py
│   │   │   ├── firewall_view.py
│   │   │   ├── cleaning_view.py
│   │   │   ├── quarantine_view.py
│   │   │   ├── settings_view.py
│   │   │   └── update_view.py
│   │   ├── main.py               # Punto de entrada de la GUI
│   │   ├── engine_bridge.py      # Puente IPC GUI ↔ Motor Rust
│   │   ├── utils.py              # Utilidades de rutas
│   │   └── requirements.txt
│   │
│   └── 📂 Instalador/            # Instalador empaquetado con PyInstaller
│
├── 📂 media/                     # Recursos gráficos (logo UPT)
├── 📄 FD01-Informe-Factibilidad.md
├── 📄 FD02-Informe-Vision.md
├── 📄 FD02-Informe-Gestion.md
├── 📄 FD03-Informe-Requerimientos.md
├── 📄 FD04-Informe-Arquitectura.md
└── 📄 README.md
```

---

## 📸 Capturas de Pantalla

> *Las capturas de pantalla se encuentran disponibles en la carpeta `media/` del repositorio.*

| Vista | Descripción |
|:------|:------------|
| ![Dashboard](media/screenshot-dashboard.png) | Dashboard principal con indicador de estado |
| ![Protection](media/screenshot-protection.png) | Módulos de protección con switches |
| ![Firewall](media/screenshot-firewall.png) | Control de firewall con perfiles de red |
| ![Quarantine](media/screenshot-quarantine.png) | Gestión de archivos en cuarentena |

*Nota: Si las imágenes no cargan, ejecutar la aplicación para ver la interfaz en tiempo real.*

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Por favor, sigue el proceso estándar:

1. **Fork** del repositorio
2. Crear rama de funcionalidad: `git checkout -b feature/nombre-funcionalidad`
3. Realizar cambios siguiendo las [convenciones de commits](#convenciones-de-commits)
4. Escribir o actualizar pruebas si aplica
5. Abrir un **Pull Request** con descripción detallada de los cambios

### Convenciones de Commits

```
feat:     Nueva funcionalidad
fix:      Corrección de error
docs:     Cambios de documentación
refactor: Refactorización sin cambio funcional
test:     Pruebas
chore:    Tareas de mantenimiento
```

### Reportar Issues

Para reportar bugs o solicitar funcionalidades, abrir un [Issue](../../issues/new) con:
- Descripción clara del problema o funcionalidad
- Pasos para reproducir (si es un bug)
- Comportamiento esperado vs. actual
- Versión del sistema operativo y de SecureGuard

---

## 👥 Equipo de Desarrollo

| Integrante | Rol | Universidad |
|:-----------|:----|:------------|
| **LLica Mamani, Jimmy Mijair** (2023076789) | Jefe de Proyecto / Desarrollador Backend | UPT |
| **Sierra Ruiz, Iker Alberto** (2023077090) | Desarrollador Frontend / QA | UPT |

**Docente:** Mag. Patrick Cuadros Quiroga — Curso: Calidad y Pruebas de Software

**Universidad Privada de Tacna** — Facultad de Ingeniería — Escuela Profesional de Ingeniería de Sistemas

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Ver el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License — Copyright (c) 2026 SecureGuard Antivirus Team
```

---

*SecureGuard Antivirus v1.0 — Universidad Privada de Tacna, 2026*
