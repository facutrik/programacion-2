class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.prestadoA = None

    def prestar(self, miembro):
        if self.disponible:
            self.disponible = False
            self.prestadoA = miembro
            return True
        else: 
            return False

    def devolver(self):
        self.disponible = True
        self.prestadoA = None

class Miembro:
    def __init__(self, nombre, id):
        self.nombre = nombre 
        self.dni = id
        self.libro_prestado = []

    def tomar_libro(self, libro):
        if libro.prestar(self):
            self.libro_prestado.append(libro)
            print(f"{self.nombre} tomo prestado '{libro.titulo}'")
        else: 
            print(f"El libro {libro.titulo} no esta disponible")

    def devolver_libro(self, libro):
        if libro in self.libro_prestado:
            libro.devolver()
            self.libro_prestado.remove(libro)
            print(f"{self.nombre} devolvio '{libro.titulo}'")
        else:
            print(f"{self.nombre} no tiene ese libro")


class Biblioteca:
    def __init__ (self):
        self.libros = []
        self.miembros = []

    def agregar_libros(self, libro):
        self.libros.append(libro)

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

    def estado_libros(self):
        print("Estado de libros: ")
        for libro in self.libros:
            if libro.disponible:
                print(f"{libro.titulo} - Disponible")
            else:
                print(f"{libro.titulo} - Prestado a {libro.prestadoA.nombre}")

    def estado_miembros(self):
        print("Estado de miembros")
        for m in self.miembros:
            for l in m.libro_prestado:
                print(f"{m.nombre} - Libros: {l.titulo}")



def main():
    biblioteca = Biblioteca()
    
    while True:
        print("\n0- Salir")
        print("1- Agregar miembro")
        print("2- Agregar libro")
        print("3- Prestar libro")
        print("4- Devolver libro")
        print("5- Consultar estado libro")
        print("6- Consultar estado miembro")

        opcion = input("\nIngrese la opcion deseada: ")


        if opcion == "1": #Agregar miembro
            nombre = input("Nombre: ")
            dni = input("Dni: ")
            miembro = Miembro(nombre, dni)
            biblioteca.agregar_miembro(miembro)


        if opcion == "2": #Agregar libro
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            isbn = input("Isbn: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregar_libros(libro)


        if opcion == "3": #Prestar libro
            dni = input("Ingrese DNI del miembro: ")
            titulo = input("Titulo del libro: ")

            miembro_encontrado = None
            libro_encontrado = None

            for m in biblioteca.miembros:
                if m.dni == dni:
                    miembro_encontrado = m

            for l in biblioteca.libros:
                if l.titulo == titulo:
                    libro_encontrado = l

            if miembro_encontrado and libro_encontrado:
                miembro_encontrado.tomar_libro(libro_encontrado)
            else:
                print("Miembro o libro no encontrado")


        if opcion == "4": #Devolver libro
            dni = input("Ingrese DNI del miembro: ")
            titulo = input("Titulo del nombre: ")

            miembro_encontrado = None
            libro_encontrado = None

            for m in biblioteca.miembros:
                if m.dni == dni:
                    miembro_encontrado = m

            for l in biblioteca.libros:
                if l.titulo == titulo:
                    libro_encontrado = l

            if miembro_encontrado and libro_encontrado:
                miembro_encontrado.devolver_libro(libro_encontrado)
            else:
                print("Miembro o libro no encontrado")

        if opcion == "5": #Consultar estado libro
            biblioteca.estado_libros()


        if opcion == "6": #Consultar estado miembro
            biblioteca.estado_miembros()

        if opcion == "0": #Salir
            break

if __name__ == "__main__":
    main()


#TypeError
#ValueError -
#IndexError - 
#KeyErorr
#AtributeError
#ModuleNotFoundError
