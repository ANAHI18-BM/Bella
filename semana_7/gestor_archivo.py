# archivo: gestor_archivo.py

class GestorArchivo:
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase.
        Se ejecuta automáticamente cuando se crea una instancia del objeto.
        Inicializa el atributo nombre_archivo y abre el archivo en modo escritura.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, 'w')
        print(f"Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir_linea(self, texto):
        """
        Método para escribir una línea en el archivo.
        """
        self.archivo.write(texto + '\n')
        print(f"Escrito en el archivo: {texto}")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta automáticamente cuando el objeto es eliminado o el programa termina.
        Cierra el archivo abierto como tarea de limpieza.
        """
        try:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")
        except AttributeError:
            # Si el archivo ya fue cerrado o no existe
            print("Archivo ya cerrado o no se pudo cerrar.")

# Bloque principal de prueba
if __name__ == "__main__":
    gestor = GestorArchivo("tarea_constructor_destructor.txt")
    gestor.escribir_linea("Esta es la primera línea.")
    gestor.escribir_linea("Esta es la segunda línea.")
    # Al finalizar el programa, se ejecuta automáticamente el destructor
