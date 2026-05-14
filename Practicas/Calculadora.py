import tkinter as tk

root = tk.Tk()
root.title("Calculadora")
root.geometry("255x305")

pantalla = tk.Entry(root, font=("Arial", 20), width=15)
pantalla.grid(row=0, column=0, columnspan=4, padx=15, pady=8, ipady=10)

boton0 = tk.Button(root, text="0", width=3, height=1, font=("Arial", 20))
boton0.grid(row=4, column=0)

botonPun = tk.Button(root, text=".", width=3, height=1, font=("Arial", 20))
botonPun.grid(row=4, column=1)

botonIg = tk.Button(root, text="=", width=3, height=1, font=("Arial", 20))
botonIg.grid(row=4, column=2)

botonPor = tk.Button(root, text="x", width=3, height=1, font=("Arial", 20))
botonPor.grid(row=4, column=3)

boton1 = tk.Button(root, text="1", width=3, height=1, font=("Arial", 20))
boton1.grid(row=3, column=0)

boton2 = tk.Button(root, text="2", width=3, height=1, font=("Arial", 20))
boton2.grid(row=3, column=1)

boton3 = tk.Button(root, text="3", width=3, height=1, font=("Arial", 20))
boton3.grid(row=3, column=2)

botonDiv = tk.Button(root, text=":", width=3, height=1, font=("Arial", 20))
botonDiv.grid(row=3, column=3)

boton4 = tk.Button(root, text="4", width=3, height=1, font=("Arial", 20))
boton4.grid(row=2, column=0)

boton5 = tk.Button(root, text="5", width=3, height=1, font=("Arial", 20))
boton5.grid(row=2, column=1)

boton6 = tk.Button(root, text="6", width=3, height=1, font=("Arial", 20))
boton6.grid(row=2, column=2)

botonMen = tk.Button(root, text="-", width=3, height=1, font=("Arial", 20))
botonMen.grid(row=2, column=3)

boton7 = tk.Button(root, text="7", width=3, height=1, font=("Arial", 20))
boton7.grid(row=1, column=0)

boton8 = tk.Button(root, text="8", width=3, height=1, font=("Arial", 20))
boton8.grid(row=1, column=1)

boton9 = tk.Button(root, text="9", width=3, height=1, font=("Arial", 20))
boton9.grid(row=1, column=2)

botonMas = tk.Button(root, text="+", width=3, height=1, font=("Arial", 20))
botonMas.grid(row=1, column=3)

root.mainloop()
