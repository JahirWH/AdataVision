# Adatavision v2

<div align="center"><img src="logo.png"></div>

**Descarga e instalación:**
- Descarga el archivo `Adatavision_exe` o click
- https://github.com/JahirWH/Adatavision/releases/download/v3.0/Adatavision_exe
- Extrae el contenido en tu carpeta preferida
- Ejecuta `adatavision.exe` directamente

## Características principales
- Gestión segura de contraseñas con cifrado avanzado (Fernet + SHA256)
- Interfaz gráfica moderna e intuitiva con PySide6
- Manejo de inventario y datos con CSV nativo
- Aplicación portable - no requiere instalación
- Generador de contraseñas y claves integrado
- Temas claro/oscuro con cambio dinámico
- Exportación e importación de datos en CSV y JSON
- Temporizador de inactividad para mayor seguridad
- Modificación de entradas existentes por código
- Barra de herramientas con acciones rápidas

## Cambios en la versión v3
- **Sistema de temas mejorado:** Se implementó `ThemeManager` para aplicar temas claro/oscuro con estilo CSS dinámico. Ahora todos los widgets tienen una apariencia coherente y configurable.
- **Nueva imagen de inicio:** Se actualizó el splash screen de `cyberpunk.png` a `taurs.png`.
- **Mejoras en la tabla de contraseñas:** Ahora las contraseñas se copian automáticamente al hacer clic, eliminando el botón de "Copiar". También se simplificó la edición de celdas.
- **Temporizador de seguridad:** Se añadió un `QTimer` que detecta inactividad del usuario y permite cerrar la sesión automáticamente.
- **Diálogo de modificación:** Nueva ventana para editar entradas existentes mediante su código, con campos para servicio, email, contraseña, usuario y referencia.
- **Exportar e importar datos:** Ahora es posible guardar y cargar información en formato CSV o JSON, útil para respaldo y migración de datos.
- **Acciones en barra de herramientas:** Se añadieron accesos rápidos a "Cambiar tema", "Exportar" e "Importar" desde una nueva `QToolBar`.
- **Código reorganizado:** Funciones auxiliares nuevas como `read_info_file`, `write_info_file`, y `update_info_field` para un manejo unificado de `info.txt`.
- **Manejo de errores mejorado:** Captura de excepciones más general para evitar bloqueos inesperados.
- **Actualización de versión:** El número de versión pasó de 2.0 a 3.0.
- **Estilo refinado:** Cambios en color de texto, tamaños de botones y consistencia visual general.

## Requisitos
- Windows 10/11 o Linux
- No requiere Python ni dependencias adicionales para el ejecutable

## Uso
Simplemente descarga el archivo `.exe` para ejecutar en windows. o descarga el `.bin` para ejecutar en linux , asegurate de darle permisos chmod +x Adatavision.bin, o de instalar las librerias en requeriments, tanto en windows como en linux.  

**Nota:** Si vienes de una versión anterior, ya no necesitas `estado.txt`, `date.txt` ni `temp.txt`. El sistema ahora utiliza solamente `info.txt` para toda la información de estado.

---
*Compilado con Nuitka para máximo rendimiento y compatibilidad*
