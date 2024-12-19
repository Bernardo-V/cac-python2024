![img](https://i.postimg.cc/FRXKcL88/comienza.gif)
# CAC-Python2024
# Sistema de Gestión de Inventario 🛒
## Descripción del proyecto 🚀
Este es un sistema sencillo de gestión de inventario, diseñado para mantener un registro de productos. Permite realizar operaciones básicas como:

- Agregar productos.
- Mostrar productos existentes.
- Actualizar cantidades.
- Eliminar productos.
- Buscar productos por ID, nombre o categoría.
- Generar reportes de bajo stock.

La aplicación utiliza **SQLite** para la base de datos y **Colorama** para mejorar la visualización en la terminal.

---
## Instalación 🚀
Sigue estos pasos para instalar y ejecutar el sistema:

1. **Clona el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```
2. **Instala las dependencias necesarias**:
   ```bash
   pip install colorama
   ```

3. **Ejecuta el programa**:
   ```bash
   python <nombre_del_archivo>.py
   ```
---
## Uso 📖
Al ejecutar el programa, aparecerá un menú principal con las siguientes opciones:

1. **Agregar producto**: Permite añadir un nuevo producto al inventario ingresando nombre, descripción, cantidad, precio y categoría.
2. **Mostrar productos**: Lista todos los productos registrados en la base de datos.
3. **Actualizar cantidad de producto**: Modifica la cantidad disponible de un producto existente mediante su ID.
4. **Eliminar producto**: Elimina un producto del inventario por su ID.
5. **Buscar producto**: Realiza búsquedas filtrando por ID, nombre o categoría.
6. **Reporte de bajo stock**: Genera un informe de productos con stock igual o inferior al límite definido por el usuario.
7. **Salir**: Cierra el programa.

---

## Estructura del Proyecto 📂

```
|-- inventario.db          # Base de datos SQLite (se genera automáticamente)
|-- app.py                 # Código principal del sistema
|-- README.md              # Documentación del proyecto
```
## Tecnologías Utilizadas 🛠️
- **Python**: Lenguaje principal.
- **SQLite**: Base de datos ligera y eficiente.
- **Colorama**: Biblioteca para mejorar la experiencia visual en la terminal.

## Integrante:
•	Velazquez, Bernardo.

## DER:

Este proyecto fué generado con 🛠️ [Python](https://www.python.org/) version 3.

## Estado del proyecto 📌
Primera versión: En esta primera iteración nos encargaremos de modelar, a nivel datos y objetos, una solución
al dominio presentado. Además, comenzaremos con el proceso de codificación de la solución.

![img](https://i.postimg.cc/zvBcCqgT/Programas-utilizados.png)

## Agradecimientos: 🎁

* A cada uno de mis compañeros, que estuvieron a toda hora 🍺/☕
* A los profes Juan Pablo Rigotti y Agustina Digiesi 🤓.
* A mi familia ❤️* 
