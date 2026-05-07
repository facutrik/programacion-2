        #Variables
'''
nombre = "anibal"
#print (nombre)
'''
        #Tipado Dinamico = 
# las variables se pueden sobre escribir con varios datos distintos

'''
edad = 50
edad = "python"
'''

        #Booleano = se debe empezar con mayusculas

"""
pagado = True
"""

        #Funciones = para definirla
"""
def hola():
        print("Soy Anibal")

        # y para ejecutarla

hola()

        #se pueden reutilizar varias veces

hola()
hola()
hola()
"""
"""
def informacion (nombre, puesto):
        print (f"soy {nombre}, y soy {puesto}")

informacion ("anibal","programador")
informacion ("trik","cogido")
"""

#el orden de los datos, se va a completar en base a ese mismo orden, no va a interpretar que anibal es el nombre y programador el puesto
# en caso de faltar un valor, habria que hacer valores pre-establecidos ej. 

'''
def informacion (nombre, puesto = "desconocido"):
        print (f"soy {nombre}, y soy {puesto}")

informacion ("anibal","programador")
informacion ("Facundo","cogido")
informacion ("Joaquin")
'''

        #funciones que retornan un valor
#sirven por ejemplo para procesar la informacion, una vez usada la funcion, nombre se almacena dentro de empleado

"""
def informacion2 (nombre):
        return nombre

empleado = informacion2 ("juan")
print (empleado)
"""

        #funciones o metodos 

"""
nombre = "pedro"

def mostrar_nombre(nombre):
        print(f"hola {nombre}")

        #metodo (se pueden usar para casos de un objeto en particular)

mostrar_nombre(nombre)

print(nombre.upper())
"""

#practicas
#def bienvenida():
#    print("hola, buenas")

#bienvenida()

#def bienvenida2 (mensaje,nombre):
#    print (f"{mensaje}, {nombre}")

#bienvenida2("bienvenido" , "Anibal")

        #Operadores

'''
print(2 + 4)
print(4 - 5)
print(6 * 1)
print(12 / 4)
print(4 + 2.9)

print(4 ** 3) #potenciacion
'''

        #suma de numero en base a contador

'''
numero = 20
print(numero)
numero += 1
print(numero)
'''

        #funciones con numeros

'''
def suma():
        print(2+2)

suma()

def suma(a = 0, b = 1):
        print(a+b)

suma (2,4)
suma (9,2)
suma (8)

def resta(a = 0, b = 1):
        print(a-b)

resta (12,5)
'''

        #arrays o listas

"""
lenguajes = ["python", "Java Script", "Java", "PHP"]

print (lenguajes)
print (lenguajes[0])#el indice arranca en 0
"""

#Ordenar los lenguajes de Forma Alfabetica
"""
lenguajes.sort()
print(lenguajes)
"""

#Acceder a un elemento del array
"""
aprendiendo= f"estoy aprendiendo {lenguajes[3]}"
print(aprendiendo)
"""

#Modificar un valor del array

"""
lenguajes[2] = "React"
print(lenguajes)
"""

#Agregar elementos a un array

"""
lenguajes.append("PHP")
print(lenguajes)
"""

#eleminar un elemento de un array

"""
del lenguajes[1]
print(lenguajes)
"""

#eleminar el ultimo valor de un arreglo
"""
lenguajes.pop()
print(lenguajes)
"""

# O posicion en especifico
"""
lenguajes.pop(0)
print(lenguajes)
"""

# O eliminar por nombre
"""
lenguajes.remove("PHP")
print(lenguajes)
"""

                #Iteradores
                
"""
lenguajes = ["python", "Java Script", "Java", "PHP"]
for lenguaje in lenguajes:
        print(lenguaje)

for lenguaje in lenguajes:
        print(f"estoy aprendiendo {lenguaje}")
"""

#for que escriba numeros

"""
for numero in range(0,10):
        print(numero)

for numero2 in range(0, 10, 3):
        print(numero2)
"""
#primero numero = 0, el inicio
#segundo numero = 10, el final de la iteracion
#tercer numero = 3, el salto entre estos

                #condicional
#  == igual a 
#  != diferente a 
#  > Mayor a 
#  >= Mayor o igual a  
#  < Menor a 
#  <= Menor o igual a

#revisar una condicion 
balance = 500

if balance > 0:
        print("puedes pagar")
else:
        print("no te alcanza")

likes = 200

if likes == 200:
        print("Excelente, tienes doscientos likes")

#if con texto
lenguaje = "python"

if lenguaje == "python":
        print("barbaro") #ver que sea igual


if not lenguaje == "PHP":
        print("barbaro") #negando que sea python

#evaluando un booleano
usuario_autenticado = True

if usuario_autenticado == True :
        print("acceso al sistema") #podes sacar el == True por que directamente ya va a analisar si es True o no

else:
        print("Debes iniciar sesion")



#creando a un diccionario simple 

cancion = {
        "artista" : "metalica", #Llave : y valor 
        "cancion" : "enter sandman", #cerrar siempre con ,
        "lanzamiento" : 1992,
        "likes" : 3000,
}

#Acceder a un unico valor
print(cancion["artista"]) #llamas al diccionario cancion, a la llave artista, para ver el valor Metalica}
print(cancion["lanzamiento"])

#Mezclar con un string
print(f"estoy escuchando a {cancion["artista"]}")

