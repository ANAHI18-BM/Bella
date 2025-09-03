from typing import List, Dict

class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self) -> str:
        return self.info[0]

    @property
    def autor(self) -> str:
        return self.info[1]

    def __repr__(self) -> str:
        return f"Libro(ISBN={self.isbn}, Título='{self.titulo}', Autor='{self.autor}', Categoría='{self.categoria}')"


class Usuario:
    def __init__(self, nombre: str, user_id: str):
        self.nombre = nombre
        self.user_id = user_id
        self.prestados: List[Libro] = []

    def __repr__(self) -> str:
        return f"Usuario(ID={self.user_id}, Nombre='{self.nombre}', Prestados={len(self.prestados)})"


class Biblioteca:
    def __init__(self):
        self.libros: Dict[str, Libro] = {}
        self.usuarios: Dict[str, Usuario] = {}
        self.user_ids: set = set()
        self.prestamos: Dict[str, str] = {}

    def anadir_libro(self, libro: Libro):
        if libro.isbn in self.libros:
            raise ValueError(f"El ISBN '{libro.isbn}' ya existe.")
        self.libros[libro.isbn] = libro
        print(f"[OK] Libro añadido: {libro}")

    def quitar_libro(self, isbn: str):
        if isbn not in self.libros:
            raise KeyError(f"ISBN '{isbn}' no encontrado.")
        if isbn in self.prestamos:
            raise ValueError(f"No se puede quitar el libro {isbn}: actualmente prestado.")
        libro = self.libros.pop(isbn)
        print(f"[OK] Libro eliminado: {libro}")

    def registrar_usuario(self, usuario: Usuario):
        if usuario.user_id in self.user_ids:
            raise ValueError(f"El ID '{usuario.user_id}' ya existe.")
        self.usuarios[usuario.user_id] = usuario
        self.user_ids.add(usuario.user_id)
        print(f"[OK] Usuario registrado: {usuario}")

    def dar_baja_usuario(self, user_id: str):
        if user_id not in self.user_ids:
            raise KeyError(f"Usuario '{user_id}' no registrado.")
        usuario = self.usuarios[user_id]
        if usuario.prestados:
            raise ValueError(f"No se puede dar de baja al usuario '{user_id}': tiene libros prestados.")
        del self.usuarios[user_id]
        self.user_ids.remove(user_id)
        print(f"[OK] Usuario '{user_id}' dado de baja.")

    def prestar_libro(self, isbn: str, user_id: str):
        if isbn not in self.libros:
            raise KeyError(f"ISBN '{isbn}' no existe.")
        if user_id not in self.user_ids:
            raise KeyError(f"Usuario '{user_id}' no registrado.")
        if isbn in self.prestamos:
            raise ValueError(f"El libro {isbn} ya está prestado.")
        libro = self.libros[isbn]
        usuario = self.usuarios[user_id]
        usuario.prestados.append(libro)
        self.prestamos[isbn] = user_id
        print(f"[OK] Prestado: {libro.titulo} -> Usuario {usuario.nombre}")

    def devolver_libro(self, isbn: str, user_id: str):
        if isbn not in self.prestamos:
            raise KeyError(f"No hay registro de préstamo para ISBN '{isbn}'.")
        if self.prestamos[isbn] != user_id:
            raise ValueError(f"El libro {isbn} no está prestado al usuario {user_id}.")
        usuario = self.usuarios[user_id]
        usuario.prestados = [b for b in usuario.prestados if b.isbn != isbn]
        del self.prestamos[isbn]
        print(f"[OK] Devolución: ISBN {isbn} por usuario {user_id}")

    def buscar_por_titulo(self, texto: str) -> List[Libro]:
        texto = texto.lower()
        return [libro for libro in self.libros.values() if texto in libro.titulo.lower()]

    def buscar_por_autor(self, texto: str) -> List[Libro]:
        texto = texto.lower()
        return [libro for libro in self.libros.values() if texto in libro.autor.lower()]

    def buscar_por_categoria(self, categoria: str) -> List[Libro]:
        categoria = categoria.lower()
        return [libro for libro in self.libros.values() if libro.categoria.lower() == categoria]

    def listar_prestados_usuario(self, user_id: str) -> List[Libro]:
        if user_id not in self.user_ids:
            raise KeyError(f"Usuario '{user_id}' no registrado.")
        return self.usuarios[user_id].prestados

    def listar_todos_libros(self) -> List[Libro]:
        return list(self.libros.values())

    def estado_biblioteca(self) -> str:
        return f"Estado Biblioteca: {len(self.libros)} libros | {len(self.user_ids)} usuarios | {len(self.prestamos)} préstamos activos"


# ---------- DEMO CON MIS DATOS ----------
def run_demo():
    print("=== DEMO: Sistema de Gestión de Biblioteca Digital ===\n")
    b = Biblioteca()

    # Libros
    libros_demo = [
        Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "B001"),
        Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "B002"),
        Libro("1984", "George Orwell", "Distopía", "B003"),
        Libro("Arte y Tecnología", "María Ruiz", "Arte", "B004"),
    ]
    for lib in libros_demo:
        b.anadir_libro(lib)
    print()

    # Usuarios
    usuarios_demo = [
        Usuario("Bella Morocho", "U001"),
        Usuario("Jose Morocho", "U002"),
    ]
    for usr in usuarios_demo:
        b.registrar_usuario(usr)
    print()

    # Préstamos
    b.prestar_libro("B001", "U001")
    b.prestar_libro("B002", "U002")
    print()

    # Listar prestados
    print("Libros prestados a U001:", b.listar_prestados_usuario("U001"))
    print("Libros prestados a U002:", b.listar_prestados_usuario("U002"))
    print()

    # Buscar libros
    print("Buscar por título 'principito':", b.buscar_por_titulo("principito"))
    print("Buscar por autor 'Orwell':", b.buscar_por_autor("Orwell"))
    print("Buscar por categoría 'Arte':", b.buscar_por_categoria("Arte"))
    print()

    # Devolver libro
    b.devolver_libro("B001", "U001")
    print("Después de devolver B001 ->", b.estado_biblioteca())
    print("Prestados U001 (ahora):", b.listar_prestados_usuario("U001"))
    print()

    # Quitar libro
    b.devolver_libro("B002", "U002")
    b.quitar_libro("B002")
    print()

    # Dar de baja usuario
    b.dar_baja_usuario("U001")
    print()

    # Estado final
    print(b.estado_biblioteca())
    print("Libros en catálogo ahora:", b.listar_todos_libros())
    print("\n=== FIN DEMO ===")


if __name__ == "__main__":
    run_demo()
