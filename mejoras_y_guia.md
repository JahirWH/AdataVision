# Guía de Mejoras para AdataVision

## Estructura Deseada

1. Cargar archivo -> String en memoria -> Desencriptar -> Modificar -> Encriptar -> Guardar archivo

## Cambios Necesarios

### 1. Variables de Estado en MainWindow

- self.datos_en_memoria (str): Contendrá los datos CSV como string
- self.datos_modificados (bool): Indica si hay cambios sin guardar
- self.estado_encriptado (bool): Indica si los datos están encriptados

### 2. Flujo Principal de Datos

```
Inicio:
   ├── Cargar CSV a memoria
   │   └── self.datos_en_memoria = leer_archivo('Inventario.csv')
   │
   ├── Desencriptar (cuando usuario lo solicite)
   │   └── self.datos_en_memoria = desencriptar(self.datos_en_memoria)
   │
   ├── Operaciones (todo en memoria)
   │   ├── Ver datos
   │   ├── Modificar
   │   ├── Agregar
   │   └── Eliminar
   │
   └── Al Cerrar
       ├── Si hay cambios:
       │   ├── Encriptar datos
       │   └── Guardar en archivo
       └── Limpiar memoria
```

### 3. Funciones a Modificar/Crear

#### Manejo de Archivo

```python
def cargar_archivo_a_memoria(self):
    """Lee Inventario.csv y lo guarda como string en memoria"""

def guardar_cambios(self):
    """Guarda los datos de memoria al archivo"""
```

#### Operaciones en Memoria

```python
def ver_datos(self):
    """Muestra datos de memoria en la tabla"""

def modificar_dato(self, nuevo_valor):
    """Modifica datos en memoria"""
    self.datos_modificados = True

def agregar_dato(self, nuevo_dato):
    """Agrega datos en memoria"""
    self.datos_modificados = True
```

#### Encriptación

```python
def encriptar_datos_memoria(self):
    """Encripta los datos en memoria"""

def desencriptar_datos_memoria(self):
    """Desencripta los datos en memoria"""
```

### 4. Orden de Implementación

1. Modificar clase principal:

   - Añadir nuevas variables de estado
   - Implementar carga inicial a memoria

2. Crear funciones de manejo de memoria:

   - Implementar conversión CSV <-> String
   - Manejar modificaciones en memoria

3. Adaptar funciones existentes:

   - Modificar funciones de ver/agregar/modificar
   - Usar datos en memoria en lugar de archivo

4. Implementar guardado automático:

   - Detectar cierre de aplicación
   - Guardar cambios si es necesario

5. Mejorar encriptación:
   - Trabajar con datos en memoria
   - Encriptar solo al guardar

### 5. Puntos de Mejora

1. Rendimiento:

   - Usar StringIO para manejar CSV en memoria
   - Implementar caché para búsquedas frecuentes

2. Seguridad:

   - Limpiar memoria después de cerrar
   - No escribir datos desencriptados en disco

3. Usabilidad:
   - Indicador de cambios sin guardar
   - Confirmación antes de cerrar con cambios

### 6. Ejemplo de Uso

```python
# Al iniciar
self.cargar_archivo_a_memoria()

# Al desencriptar
self.desencriptar_datos_memoria()
self.mostrar_datos()

# Al modificar
self.modificar_dato(nuevo_valor)  # Automáticamente marca como modificado

# Al cerrar
if self.datos_modificados:
    self.encriptar_datos_memoria()
    self.guardar_cambios()
self.limpiar_memoria()
```

### 7. Consideraciones

1. Mantener respaldo de datos antes de modificar
2. Validar datos antes de guardar
3. Manejar errores de memoria
4. Implementar auto-guardado periódico (opcional)
5. Mostrar indicador de estado (encriptado/modificado)
6. Implementar la eliminacion de celdas
7. implementar ocultacion de celdas o filtro

### 8. Próximos Pasos

1. Implementar el manejo básico en memoria
2. Adaptar funciones existentes
3. Probar con datos de ejemplo
4. Implementar encriptación
5. Añadir manejo de errores
6. Mejorar interfaz de usuario
7. IMplementacion de estatus activo e inactivo
