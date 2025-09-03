class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_info(self):
        return {
            "ID": self.id,
            "Nombre": self.nombre,
            "Cantidad": self.cantidad,
            "Precio": self.precio
        }

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio
