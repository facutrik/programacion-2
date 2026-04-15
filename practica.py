import random
from enum import Enum

# 1. Definición de la Enumeración
class Sexo(Enum):
    MASCULINO = "H"
    FEMENINO = "M"

# 2. Definición de la Clase Persona
class Persona:
    # Constructor con DOBLE guion bajo
    def __init__(self, nombre="", edad=0, sexo=Sexo.FEMENINO, peso=0.0, altura=0.0):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__dni = self.__genera_dni()

    # Método privado con DOBLE guion bajo
    def __genera_dni(self):
        return str(random.randint(10000000, 99999999))

    # --- GETTERS ---
    def get_nombre(self): return self.__nombre
    def get_edad(self): return self.__edad
    def get_sexo(self): return self.__sexo
    def get_peso(self): return self.__peso
    def get_altura(self): return self.__altura
    def get_dni(self): return self.__dni

    # --- SETTERS ---
    def set_nombre(self, nombre): self.__nombre = nombre
    def set_edad(self, edad): self.__edad = edad
    def set_sexo(self, sexo): self.__sexo = sexo
    def set_peso(self, peso): self.__peso = peso
    def set_altura(self, altura): self.__altura = altura

    # Métodos de lógica
    def calcular_imc(self):
        if self.__altura > 0:
            # Usando DOBLE guion bajo para acceder a las variables
            return self.__peso / (self.__altura ** 2)
        return 0

    def valorar_peso_corporal(self):
        imc = self.calcular_imc()
        if imc < 18:
            return -1
        elif 18 <= imc <= 25:
            return 0
        else:
            return 1

    def es_mayor_de_edad(self):
        return self.__edad >= 18

    # Método para imprimir con DOBLE guion bajo
    def __str__(self):
        return (f"Persona[Nombre: {self.__nombre}, Edad: {self.__edad}, "
                f"DNI: {self.__dni}, Sexo: {self.__sexo.name}, "
                f"Peso: {self.__peso}kg, Altura: {self.__altura}m]")

# 3. Función Ejecutable (Fuera de la clase)
def ejecutar():
    print("--- Introduce los datos de la persona ---")
    try:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        sexo_input = input("Sexo (H/M): ").upper()
        sexo = Sexo.MASCULINO if sexo_input == "H" else Sexo.FEMENINO
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))

        # OBJETO 1
        p1 = Persona(nombre, edad, sexo, peso, altura)

        # OBJETO 2
        p2 = Persona(nombre, edad, sexo)

        # OBJETO 3
        p3 = Persona()
        p3.set_nombre("Celia")
        p3.set_edad(25)
        p3.set_sexo(Sexo.FEMENINO)
        p3.set_peso(60.0)
        p3.set_altura(1.70)

        lista_personas = [p1, p2, p3]

        for i, p in enumerate(lista_personas, 1):
            print(f"\n--- Resultados Persona {i} ---")
            
            res = p.valorar_peso_corporal()
            if res == -1:
                print("Estado: Por debajo del peso ideal.")
            elif res == 0:
                print("Estado: En su peso ideal.")
            else:
                print("Estado: Tiene sobrepeso.")

            print("Es mayor de edad." if p.es_mayor_de_edad() else "Es menor de edad.")
            
            print(p)

    except ValueError:
        print("Error: Por favor, introduce números válidos para edad, peso y altura.")

# Bloque principal de ejecución con DOBLE guion bajo
if __name__ == "__main__":
    ejecutar()
