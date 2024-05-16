from tkinter import messagebox

def validar(var2):
    try:
        edad = int(var2.get())
        if edad >= 18:
            messagebox.showinfo("Resultado", "Eres un adulto.")
        else:
            messagebox.showinfo("Resultado", "Aún no eres un adulto.")
    except ValueError as e:
        messagebox.showerror("Error", f"¡Debes ingresar un número válido para la edad!\nError: {e}")
