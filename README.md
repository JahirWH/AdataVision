
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Security-AES-important)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub%20Actions-blue)

<div align="center"><img src="logo.png"></div>

AdataVision es un gestor de contraseñas con interfaz gráfica que almacena y protege tus credenciales usando cifrado Fernet seguro. Las claves de cifrado se generan automáticamente a partir del usuario y contraseña, sin guardarlas en disco.

## Capturas de Pantalla

<div align="center"><img src="cap1.webp"></div>
<div align="center"><img src="cap2.webp"></div>

## Características Principales

- **Sistema de autenticación** con usuario personal
- **Cifrado Fernet** para protección de datos
- **Generador integrado** de contraseñas seguras
- **Búsqueda avanzada** con filtrado rápido
- **Copia al portapapeles** para acceso rápido
- **Auto-encriptación** al cerrar la aplicación

## Instalación y Ejecución

### Opción 1: Desde el código fuente
```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/AdataVision.git
cd AdataVision

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la aplicación
python Adatavision.py
```

### Opción 2: Instalación con pip
```bash
# Instalar desde el repositorio
pip install git+https://github.com/JahirWH/AdataVision.git

# Ejecutar
adatavision
```

### Opción 3: Ejecutable precompilado
```bash
# Dar permisos de ejecución
chmod +x ./Adatavision.bin

# Ejecutar
./Adatavision.bin
```

## Requisitos del Sistema

- Python 3.10 o superior
- PySide6 >= 6.5.0
- cryptography >= 41.0.0

## Desarrollo

### Configuración del entorno de desarrollo
```bash
# Clonar el repositorio
git clone https://github.com/jahiwWH/AdataVision.git
cd AdataVision

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias de desarrollo
pip install -r requirements.txt
pip install -r requirements-test.txt
```

### Ejecutar tests
```bash
# Tests unitarios
pytest

# Tests con cobertura
pytest --cov=.

# Linting
flake8 .
```

### CI/CD

El proyecto utiliza GitHub Actions para CI/CD automático:

- **Tests automáticos** en Python 3.10 y 3.11
- **Verificación de sintaxis** de todos los archivos Python
- **Linting** con flake8
- **Build automático** en pushes a main/master

El workflow se ejecuta en:
- Push a ramas `main` o `master`
- Pull requests a `main` o `master`

## Estructura del Proyecto

```
AdataVision/
├── Adatavision.py          # Aplicación principal
├── test_adatavision.py     # Tests unitarios
├── requirements.txt        # Dependencias principales
├── requirements-test.txt   # Dependencias de testing
├── pytest.ini            # Configuración de pytest
├── pyproject.toml        # Configuración moderna de Python
├── setup.py              # Configuración de instalación
├── tox.ini               # Configuración de testing local
└── .github/workflows/    # Configuración de CI/CD
    └── python-app.yml
```

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Guías de contribución

- Asegúrate de que todos los tests pasen
- Sigue las convenciones de código (flake8)
- Añade tests para nuevas funcionalidades
- Actualiza la documentación según sea necesario

## Licencia

MIT License - ver el archivo [LICENSE](LICENSE) para más detalles.
