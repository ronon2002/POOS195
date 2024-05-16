from tkinter import Tk, Frame, Button, Label, Entry
import tkinter as tk
from ValueError import validar

Ventana = Tk()
Ventana.title("password")
Ventana.geometry("600x400")

seccion1 = Frame(Ventana)
seccion1.pack(expand=True, fill='both')

Label(seccion1, text="Value Error", bg="black", fg="white", font=("Mono", 18)).pack()

var1 = tk.StringVar()
Label(seccion1, text="Nombre:", font=("Helvetica", 14)).pack()
Entry(seccion1, takefocus=True, textvariable=var1).pack()

var2 = tk.StringVar()
Label(seccion1, text="Edad:", font=("Helvetica", 14)).pack()
Entry(seccion1, textvariable=var2).pack()

botonAcceso = Button(seccion1, text="Evaluar", command=lambda: validar(var2))
botonAcceso.pack()

Ventana.mainloop()