# archivo: inventario.py
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Validar ID único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print(" Producto añadido correctamente.")

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print(" Producto eliminado.")
                return
        print(" No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print(" Producto actualizado.")
                return
        print(" No se encontró un producto con ese ID.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print(" No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print(" El inventario está vacío.")
        else:
            print(" Inventario actual:")
            for p in self.productos:
                print(p)
