class Estudiantes():
    def __init__(self, nombre, apellido, nroMat, carrera): #registro de estudiantes
        self.nombre = nombre
        self.apellido = apellido
        self.nroMat = nroMat
        self.carrera = carrera
        self.inscriptosEn = []

    def inscribirse(self):
        print

    def darseBaja(self):
        print

    def estadoEstCursos(self):
        print

class Curso():
    def __init__(self, nomCurso, codCurso, profEncargado): #registro de cursos
        self.nomCurso = nomCurso
        self.codCurso = codCurso
        self.profEncargado = profEncargado
        self.alumnosInscriptos = []

    def agregarEst(self):
        print

    def eliminarEst(self):
        print
    
    def hayCupos(self):
        print

    def estado(self):
        print

class Facultad():
    def __init__(self, capacidadMax):
        self.estudiantes = []
        self.cursos = []
        self.capacidadMax = capacidadMax
