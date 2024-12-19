import sqlite3
from colorama import Fore, Style, init
init(autoreset=True)

def conectar_db():
    """Conecta a la base de datos SQLite y crea la tabla si no existe."""
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    ''')
    conn.commit()
    return conn

def agregar_producto(conn):
    """Agrega un nuevo producto al inventario."""
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese una descripcion del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoria del producto: ")

    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, descripcion, cantidad, precio, categoria))
    conn.commit()
    print(Fore.GREEN + "Producto agregado con éxito!")

def mostrar_productos(conn):
    """Muestra todos los productos del inventario."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if productos:
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, "
                  f"Cantidad: {producto[3]}, Precio: {producto[4]:.2f}, Categoría: {producto[5]}")
    else:
        print(Fore.YELLOW + "No hay productos en el inventario.")

def actualizar_cantidad(conn):
    """Actualiza la cantidad de un producto específico por su ID."""
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_producto))
    if cursor.rowcount > 0:
        conn.commit()
        print(Fore.GREEN + "Cantidad actualizada con éxito!")
    else:
        print(Fore.RED + "No se encontró el producto con el ID especificado.")

def eliminar_producto(conn):
    """Elimina un producto del inventario por su ID."""
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))

    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    if cursor.rowcount > 0:
        conn.commit()
        print(Fore.GREEN + "Producto eliminado con éxito!")
    else:
        print(Fore.RED + "No se encontró el producto con el ID especificado.")

def buscar_producto(conn):
    """Busca un producto en el inventario por ID, nombre o categoría."""
    criterio = input("Buscar por (id/nombre/categoria): ").strip().lower()
    valor = input("Ingrese el valor a buscar: ")

    cursor = conn.cursor()
    if criterio == "id":
        cursor.execute("SELECT * FROM productos WHERE id = ?", (valor,))
    elif criterio == "nombre":
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{valor}%",))
    elif criterio == "categoria":
        cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", (f"%{valor}%",))
    else:
        print(Fore.RED + "Criterio de búsqueda no válido.")
        return

    resultados = cursor.fetchall()
    if resultados:
        for producto in resultados:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, "
                  f"Categoría: {producto[3]}, Cantidad: {producto[4]:.2f}, Precio: {producto[5]}")
    else:
        print(Fore.YELLOW + "No se encontraron productos que coincidan con la búsqueda.")

def reporte_bajo_stock(conn):
    """Genera un reporte de productos con bajo stock."""
    limite = int(input("Ingrese el límite de stock: "))

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    if productos:
        print(Fore.BLUE + "\nProductos con bajo stock:")
        print(Fore.GREEN + f"{'ID':<10}{'Nombre':<20}{'Cantidad':<10}")
        print("-" * 40)
        for producto in productos:
            print(f"{producto[0]:<10}{producto[1]:<20}{producto[3]:<10}")
    else:
        print(Fore.YELLOW + "No hay productos con bajo stock.")


def menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    conn = conectar_db()

    while True:
        print(Fore.CYAN + "\nMenú Principal:")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Actualizar cantidad de producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de bajo stock")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto(conn)
        elif opcion == "2":
            mostrar_productos(conn)
        elif opcion == "3":
            actualizar_cantidad(conn)
        elif opcion == "4":
            eliminar_producto(conn)
        elif opcion == "5":
            buscar_producto(conn)
        elif opcion == "6":
            reporte_bajo_stock(conn)
        elif opcion == "7":
            print(Fore.GREEN + "Gracias por usar el sistema de inventario.")
            conn.close()
            break
        else:
            print(Fore.RED + "Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()