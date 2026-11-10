# Representa un libro y guarda su nombre.
class Libro:
    def __init__(self, nombre):
        self.nombre = nombre

    # Muestra informacion del libro.
    def mostrar_info(self):
        print("Nombre:", self.nombre)


# Clase derivada que hereda las carecteristias de la clase Libro.
class LibroFisico(Libro):
    def __init__(self, nombre, encuadernacion):
        super().__init__(nombre)  # Utiliza el constructor de Libro.
        self.encuadernacion = encuadernacion

    # Metodo para mostrar el tipo de encuadernacion.
    def mostrar_encuadernacion(self):
        print("Encuadernacion:", self.encuadernacion)

    # Sobrescribe el metodo de la clase principal y agrega informacion nueva.
    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo: Libro fisico")
        self.mostrar_encuadernacion()


# Clase derivada que hereda las carecteristias de la clase Libro.
class LibroDigital(Libro):
    def __init__(self, nombre, formato):
        super().__init__(nombre)  # Utiliza el constructor de Libro.
        self.formato = formato

    # Metodo para mostrar el formato.
    def mostrar_formato(self):
        print("Formato:", self.formato)

    # Sobrescribe el metodo de la clase principal y agrega informacion nueva.
    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo: Libro digital")
        self.mostrar_formato()


# Administra los libros de la biblioteca.
class Biblioteca:
    def __init__(self):
        self.libros = []  # Lista donde se van a guardar los libros.

    # Agrega un nuevo libro a la lista.
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregado correctamente.")

    # Te enseña todos los libros que agregaste.
    def lista_de_libros(self):
        if len(self.libros) == 0:
            print("No hay libros registrados.")
        else:
            for libro in self.libros:
                print("-------------------")
                libro.mostrar_info()

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


# Se crea el objeto que utilizara el programa para administrar los libros en una biblioteca nueva con lista vacia.
biblioteca = Biblioteca()

# Mantiene el menu activo hasta elegir la opcion de salir.
while True:
    print("\n=== 📚 Libros leídos ===")
    print(" 1. Agregar libro físico 📝")
    print(" 2. Agregar libro digital 📝")
    print(" 3. Ver libros 📖")
    print(" 4. Buscar libro 🔍")
    print(" 5. Eliminar libro 🗑️")
    print(" 6. Salir 👋")

    opcion = input("Elige una opción: ")

    # Ejecuta la accion segun la opcion elegida.
    if opcion == "1":
        nombre = input("Nombre del libro: ")

        if nombre:
            encuadernacion = input("Encuadernacion (Pasta dura o Pasta blanda): ")
            libro = LibroFisico(nombre, encuadernacion)
            biblioteca.agregar_libro(libro)
        else:
            print("El nombre no puede estar vacío.")

    elif opcion == "2":
        nombre = input("Nombre del libro: ")

        if nombre:
            formato = input("Formato del libro (PDF, EPUB, etc.): ")
            libro = LibroDigital(nombre, formato)
            biblioteca.agregar_libro(libro)
        else:
            print("El nombre no puede estar vacío.")

    elif opcion == "3":
        biblioteca.lista_de_libros()

    elif opcion == "4":
        nombre = input("Libro a buscar: ")
        biblioteca.buscar_libro(nombre)

    elif opcion == "5":
        nombre = input("Libro a eliminar: ")
        biblioteca.eliminar_libro(nombre)

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
