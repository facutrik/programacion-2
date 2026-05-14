import tkinter as tk

root = tk.Tk()
root.title("Calculadora")
root.geometry("253x305")

pantalla = tk.Entry(root, font=("Arial", 20), width=11)
pantalla.grid(row=0, column=0, columnspan=3, padx=10, pady=8, ipady=10)

def agregar(valor):
    pantalla.insert(tk.END, valor)

def calcular():
    expresion = pantalla.get()
    resultado = eval(expresion)
    pantalla.delete(0, tk.END)
    pantalla.insert(0, resultado)

def borrar():
    pantalla.delete(0, tk.END)

numeros = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", ".", "="]
columna = 0
fila = 1
for numero in numeros:
    if numero == "=":
        accion = calcular
    else:
        accion = lambda x=numero: agregar(x)
    botonN = tk.Button(root, text=numero, width=3, height=1, font=("Arial", 20), command=accion)
    botonN.grid(row=fila, column=columna)
    columna += 1
    if columna > 2:
        columna = 0
        fila += 1

operadores = ["+", "-", "*", "/"]
fila = 1
for operador in operadores:
    botonO = tk.Button(root, text = operador, width=3, height=1, font=("Arial", 20), command=lambda x=operador:agregar(x))
    botonO.grid(row=fila, column=3)
    fila += 1

botonBorr = tk.Button(root, text = "C", width=3, height=1, font=("Arial", 20), command=borrar)
botonBorr.grid(row=0, column=3)

root.mainloop()
