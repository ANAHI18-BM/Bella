import json
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para búsqueda rápida por ID

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.id] = producto
            print(f"Producto '{producto.nombre}' agregado correctamente.")

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            eliminado = self.productos.pop(producto_id)
            print(f"Producto '{eliminado.nombre}' eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)
            print(f"Producto '{producto.nombre}' actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p.obtener_info() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto.obtener_info())
        else:
            print("El inventario está vacío.")

    def guardar_archivo(self, nombre_archivo):
        data = {pid: p.obtener_info() for pid, p in self.productos.items()}
        with open(nombre_archivo, "w") as archivo:
            json.dump(data, archivo, indent=4)
        print("Inventario guardado en archivo.")

    def cargar_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r") as archivo:
                data = json.load(archivo)
                for pid, info in data.items():
                    self.productos[pid] = Producto(info["ID"], info["Nombre"], info["Cantidad"], info["Precio"])
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado, iniciando inventario vacío.")
