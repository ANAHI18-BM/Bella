# archivo: inventario.py
from producto import Producto
import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()  # Al iniciar, carga productos si el archivo existe

    # ----------------------------
    # Métodos de persistencia
    # ----------------------------
    def guardar_en_archivo(self):
        """Guarda todos los productos en un archivo de texto"""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
            return True, "Inventario guardado correctamente."
        except PermissionError:
            return False, "Error: No tienes permisos para escribir en el archivo."
        except Exception as e:
            return False, f"Error inesperado al guardar: {e}"

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo, si existe"""
        if not os.path.exists(self.archivo):
            # Si no existe, lo crea vacío
            try:
                with open(self.archivo, "w", encoding="utf-8") as f:
                    pass
                print(f"[INFO] Archivo '{self.archivo}' creado vacío.")
            except Exception as e:
                print(f"[ERROR] No se pudo crear el archivo: {e}")
            return

        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        id, nombre, cantidad, precio = linea.strip().split(",")
                        producto = Producto(id, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
                    except ValueError:
                        print(f"[AVISO] Línea corrupta ignorada: {linea.strip()}")
        except PermissionError:
            print("[ERROR] No tienes permisos para leer el archivo de inventario.")
        except Exception as e:
            print(f"[ERROR] Error inesperado al leer archivo: {e}")

    # ----------------------------
    # Métodos de Inventario
    # ----------------------------
    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        ok, msg = self.guardar_en_archivo()
        print("✅" if ok else "❌", msg)

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                ok, msg = self.guardar_en_archivo()
                print("✅" if ok else "❌", msg)
                return
        print(" No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                ok, msg = self.guardar_en_archivo()
                print("✅" if ok else "❌", msg)
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
