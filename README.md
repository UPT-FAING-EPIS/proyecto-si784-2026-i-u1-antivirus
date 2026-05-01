# SecureGuard Antivirus

Proyecto universitario de antivirus híbrido Python + Rust.

## Requisitos
- Rust: https://rustup.rs
- Python 3.11: https://python.org
- LLVM: https://github.com/llvm/llvm-project/releases
- Visual Studio Build Tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/

## Instalación

```bash
# Compilar motor
cd backend_rust
cargo build --release

# Instalar dependencias Python
cd ../frontend_python
pip install -r requirements.txt

# Ejecutar
python main.py