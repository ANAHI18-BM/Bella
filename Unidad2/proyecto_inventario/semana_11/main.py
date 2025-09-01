from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()
    inventario.cargar_archivo("inventario.json")

    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pid = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(pid, nombre, cantidad, precio))

        elif opcion == "2":
            pid = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(pid)

        elif opcion == "3":
            pid = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(pid, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            inventario.guardar_archivo("inventario.json")
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
