# Representa un libro y guarda su nombre.
class Libro:
    def __init__(self, nombre):
        self.nombre = nombre


# Administra los libros de la biblioteca.
class Biblioteca:
    def __init__(self):
        self.libros = []  # Lista donde se van a guardar los libros.

    # Agrega un nuevo libro a la lista.
    def agregar_libro(self, nombre):
        libro = Libro(nombre)
        self.libros.append(libro)
        print("Libro agregado correctamente.")

    # Te enseña todos los libros que agregaste.
    def lista_de_libros(self):
        if len(self.libros) == 0:
            print("No hay libros registrados.")
        else:
            for libro in self.libros:
                print("-", libro.nombre)

    # Busca un libro sin importar si escribes en mayusculas o minusculas.
    def buscar_libro(self, nombre):
        for libro in self.libros:
            if libro.nombre.lower() == nombre.lower():
                print("El libro existe.")
                return

        print("El libro no existe.")

    # Busca y elimina el libro que selecciones.
    def eliminar_libro(self, nombre):
        for libro in self.libros:
            if libro.nombre.lower() == nombre.lower():
                self.libros.remove(libro)
                print("Libro eliminado correctamente.")
                return

        print("El libro no está registrado.")


# Crea el objeto que utilizara el programa para administrar los libros en una biblioteca nueva con lista vacia.
biblioteca = Biblioteca()

# Mantiene el menu activo hasta elegir la opcion de salir.
while True:
    print("\n=== 📚 Libros leídos ===")
    print(" 1. Agregar libro 📝")
    print(" 2. Ver libros 📖")
    print(" 3. Buscar libro 🔍")
    print(" 4. Eliminar libro 🗑️")
    print(" 5. Salir 👋")

    opcion = input("Elige una opción: ")

    # Ejecuta la accion segun la opcion elegida.
    if opcion == "1":
        nombre = input("Nombre del libro: ")
        if nombre:
            biblioteca.agregar_libro(nombre)
        else:
            print("El nombre no puede estar vacío.")

    elif opcion == "2":
        biblioteca.lista_de_libros()

    elif opcion == "3":
        nombre = input("Libro a buscar: ")
        biblioteca.buscar_libro(nombre)

    elif opcion == "4":
        nombre = input("Libro a eliminar: ")
        biblioteca.eliminar_libro(nombre)

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
