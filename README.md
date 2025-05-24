#  AdataVision - Gestor Seguro de Contraseñas

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Security-Fernet-important)

AdataVision es un gestor de contraseñas con interfaz gráfica moderna, diseñado para almacenar y gestionar credenciales de forma segura utilizando cifrado Fernet (AES-128 en modo CBC).


##  Funcionalidades

-  **Sistema de Login**: Autenticación mediante usuario personal
-  **Encriptación**: Protección de datos mediante cifrado Fernet
-  **Gestión de Contraseñas**: Almacenamiento seguro de credenciales
-  **Generador de Contraseñas**: Creación de contraseñas seguras
-  **Búsqueda Avanzada**: Filtrado rápido de credenciales
-  **Portapapeles**: Copia rápida de contraseñas
-  **Auto-encriptación**: Protección automática al cerrar

##  Instalación

```bash
# Clonar repositorio
git clone https://github.com/jahirWH/AdataVision.git

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
/bin/pythin3 ./Adatavision.py
python3 Adatavision.py
```

##  Requisitos

- Python 3.8 o superior
- PySide6
- cryptography
- polars

## 📝 Notas

- Las contraseñas se almacenan en formato CSV (opcional, no se guarda)
- El archivo se encripta automáticamente al cerrar
- Se requiere el usuario original y contrasena para desencriptar
