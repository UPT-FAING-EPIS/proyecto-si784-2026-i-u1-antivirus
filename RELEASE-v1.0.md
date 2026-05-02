# 🚀 Release v1.0 — SecureGuard Antivirus

**Fecha de lanzamiento:** 30 de mayo de 2026  
**Tag:** `v1.0`  
**Tipo:** Release estable — Producto Mínimo Viable (MVP)

---

## 📦 Descargas

| Archivo | Plataforma | Descripción |
|:--------|:----------:|:------------|
| `BitCraft_Antivirus_v1.0_Setup.exe` | Windows 10/11 x64 | Instalador completo con GUI + Motor |
| `secureguard_engine_v1.0.exe` | Windows 10/11 x64 | Motor standalone (CLI) |
| `Source code (zip)` | — | Código fuente completo |
| `Source code (tar.gz)` | — | Código fuente completo |

---

## 🎉 Novedades de la Versión v1.0

Esta es la **primera versión estable** de SecureGuard Antivirus, el Producto Mínimo Viable (MVP) del proyecto académico desarrollado en la Universidad Privada de Tacna.

### Motor de Seguridad (Rust)

- **Escaneo por hash SHA-256:** El motor carga en memoria las firmas del archivo `malware_hashes.txt` al inicio y las compara con los hashes de cada archivo escaneado. Las coincidencias se reportan con confianza 1.0.
- **Análisis heurístico de entropía:** Los archivos PE (ejecutables Windows) con entropía superior a 7.5 bits/byte son marcados como sospechosos (indicativo de ofuscación o empaquetado malicioso).
- **Detección por strings sospechosos:** Se analizan los primeros 4096 bytes de cada archivo buscando cadenas asociadas a técnicas de malware conocidas (`CreateRemoteThread`, `VirtualAllocEx`, `WriteProcessMemory`, `powershell -enc`, `Invoke-Mimikatz`, `ransom`, `bitcoin_wallet`).
- **Modo daemon:** El motor opera en modo persistente leyendo comandos JSON por `stdin` y escribiendo respuestas y eventos por `stdout`.
- **Protección en tiempo real:** Monitoreo de los directorios Documentos, Descargas y `C:\Users\Public` con detección y cuarentena automática.

### Gestión de Cuarentena

- Archivos detectados son movidos a `C:\ProgramData\SecureGuard\Quarantine\` como `<sha256>.quar`
- Metadatos de ruta original almacenados en archivos `.meta` para permitir restauración
- Operaciones disponibles: listar, restaurar (devolver a ubicación original) y eliminar definitivamente

### Control del Firewall

- Vista dedicada `FirewallView` para gestión del Firewall de Windows
- Activación/desactivación mediante `netsh advfirewall set allprofiles state on/off`
- Indicadores visuales por perfil de red (Dominio, Privado, Público) que reflejan el estado actual
- Manejo de errores con reversión del switch si el comando falla

### Limpieza del Sistema

- Eliminación de archivos temporales de `C:\Windows\Temp` y `%TEMP%`
- Reporte del número de archivos/carpetas eliminados

### Actualización de Firmas

- Descarga de `malware_hashes.txt` y `yara_rules.yar` desde repositorio remoto
- Almacenamiento en directorio `signatures/` local
- Manejo de errores de conectividad con mensajes descriptivos

### Interfaz Gráfica (Python/CustomTkinter)

- Tema oscuro moderno con sidebar de navegación
- **Dashboard:** Indicador de estado circular (verde/rojo), botón de escaneo rápido, barra de progreso
- **Protección:** Switches para protección en tiempo real, anti-ransomware y monitoreo de comportamiento
- **Firewall:** Vista dedicada con estado por perfil de red
- **Limpieza:** Vista con botón de limpieza y retroalimentación de resultado
- **Cuarentena:** Listado de archivos aislados con acciones de restaurar/eliminar
- **Actualizar:** Vista de actualización de firmas con feedback
- **Configuración:** Métricas del sistema (CPU, RAM, disco) usando `psutil`

---

## 🔧 Mejoras Respecto a Versiones Previas

| Área | Cambio |
|:-----|:-------|
| **FirewallView** | Vista de firewall independiente (reemplaza workaround `SettingsView(only_firewall=True)`) |
| **Estado de firewall** | Indicadores por perfil (Dominio/Privado/Público) actualizan dinámicamente según estado |
| **SettingsView** | Removida lógica de firewall; solo muestra información del sistema |
| **`except` bare** | Reemplazado `except:` por `except (OSError, PermissionError):` en SettingsView |
| **EngineBridge** | Rollback del switch de firewall si el comando del motor falla |

---

## 🐛 Problemas Conocidos

| ID | Descripción | Workaround |
|:---|:------------|:-----------|
| BUG-01 | La vista de cuarentena muestra "Función no implementada" si el motor no está corriendo | Verificar que el motor esté iniciado antes de navegar a cuarentena |
| BUG-02 | La URL de actualización de firmas tiene placeholder `TU_USUARIO` | Configurar la URL real en `updater.rs` antes de compilar |
| BUG-03 | El monitoreo en tiempo real no se puede detener sin reiniciar la aplicación | Planificado para v1.1 |
| BUG-04 | Sin notificaciones de escritorio cuando la ventana está minimizada | Planificado para v1.1 con `plyer` |

---

## 📋 Cambios en Documentación

- **FD01-Informe-Factibilidad.md:** Agregado análisis de costos en nube (AWS/Azure) y ejemplo Terraform IaC (§4.2.6, §4.2.7)
- **FD02-Informe-Gestion.md:** Nuevo — Gestión GitHub, GitFlow, roadmap, GitHub Projects
- **FD03-Informe-Requerimientos.md:** Nuevo — Historias de usuario, criterios Gherkin, diagramas de secuencia Mermaid
- **FD04-Informe-Arquitectura.md:** Nuevo — Diagramas de clases, BD, componentes y despliegue
- **README.md:** Renovado completamente con guía profesional de instalación y uso
- **wiki/**: Páginas Home, Características, Instalación, Arquitectura y Roadmap
- **ISSUES.md:** 8 issues formalizados en user story + Gherkin

---

## 🏫 Información del Proyecto

| Campo | Valor |
|:------|:------|
| **Proyecto** | SecureGuard Antivirus |
| **Universidad** | Universidad Privada de Tacna |
| **Curso** | Calidad y Pruebas de Software |
| **Docente** | Mag. Patrick Cuadros Quiroga |
| **Desarrolladores** | LLica Mamani, Jimmy Mijair (2023076789) / Sierra Ruiz, Iker Alberto (2023077090) |
| **Año** | 2026 |

---

## 🔮 Próxima Versión

La versión **v1.1** está planificada para el 31 de julio de 2026 e incluirá:

- Pipeline CI/CD con GitHub Actions
- Cobertura de pruebas unitarias >= 80%
- Notificaciones nativas de escritorio
- Historial de escaneos
- Actualizaciones automáticas programadas

Ver el [Roadmap completo](wiki/Roadmap.md) para más detalles.

---

*SecureGuard Antivirus v1.0 — Universidad Privada de Tacna — 2026*
