# tienda.py

# Esta clase representa un producto con nombre y precio
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"{self.nombre}: ${self.precio}")

# Esta clase representa un cliente con un carrito de compras
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)
        print(f"{producto.nombre} agregado al carrito.")

    def ver_carrito(self):
        print(f"Carrito de {self.nombre}:")
        for p in self.carrito:
            p.mostrar()

# ---------- Parte de ejecución del programa ---------------
p1 = Producto("Zapatos", 35)
p2 = Producto("Camisa", 20)

cliente1 = Cliente("Bella")
cliente1.agregar_al_carrito(p1)
cliente1.agregar_al_carrito(p2)
cliente1.ver_carrito()

