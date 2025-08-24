# archivo: main.py
from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()

    while True:
        print("\n===== MENÚ INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no se cambia): ")
            precio = input("Nuevo precio (dejar vacío si no se cambia): ")
            inventario.actualizar_producto(
                id,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print(" Guardando inventario antes de salir...")
            inventario.guardar_en_archivo()
            print(" Saliendo del sistema...")
            break

        else:
            print("⚠ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
