import random
import string
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox
from Password import *


class Password:
    def __init__(self, longitud = 8, mayus = False, especiales = False):
        self.longitud = longitud
        self.mayus = mayus
        self.especiales = especiales
        
        
    def generador(self):
        letras = string.ascii_letters
        digitos = string.digits
        password  = letras + digitos
        if self.mayus == True:
            password += string.ascii_uppercase
        if self.especiales == True:
            password += string.punctuation
        p = ''.join(random.choice(password) for i in range(self.longitud))
        return p
    
    def fortaleza(self):
        fort = 'media'
        if self.longitud > 9:
            fort = 'media alta'
        elif self.longitud > 9 and (self.mayus == True or self.especiales == True):
            fort = 'Alta'
        elif self.longitud > 9 and self.mayus == True and self.especiales == True:
            fort = 'Muy alta'
        
        print(messagebox.showinfo('Info', fort))
            

class interfaz:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas")

        self.password_generador = Password()

        self.widgets()

    def widgets(self):
        self.longitud = tk.Label(self.root, text="Longitud de contraseña:")
        self.longitud.grid(row=0, column=0, padx=10, pady=5)

        self.linea_long = tk.Entry(self.root)
        self.linea_long.grid(row=0, column=1, padx=10, pady=5)
        self.linea_long.insert(0, "8")

        self.mayuscula = tk.BooleanVar()
        self.mayuscula_checkbox = tk.Checkbutton(self.root, text="Incluir Mayúsculas", variable=self.mayuscula)
        self.mayuscula_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.especiales = tk.BooleanVar()
        self.especial_checkbox = tk.Checkbutton(self.root, text="Incluir Caracteres Especiales", variable=self.especiales)
        self.especial_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.boton = tk.Button(self.root, text="Generar Contraseña", command=self.password)
        self.boton.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        
        self.boton2 = tk.Button(self.root, text="Comprobar fortaleza", command= lambda: self.password_generador.fortaleza)
        self.boton.grid(row=3, column=0, columnspan=3, padx=12, pady=7)

        self.contra_label = tk.Label(self.root, text="Tu contraseña es:")
        self.contra_label.grid(row=4, column=0, padx=10, pady=5)

        self.password_entry = tk.Entry(self.root, width=30)
        self.password_entry.grid(row=4, column=1, padx=10, pady=5)

    def password(self):
        try:
            lon = int(self.linea_long.get())
            may = self.mayuscula.get()
            esp = self.especiales.get()

            self.password_generador = Password(lon,may,esp)
            password = self.password_generador.generador()

            messagebox.showinfo("Contraseña Generada", f"Su contraseña es: {password}")
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese una longitud válida.")

def main():
    root = tk.Tk()
    app = interfaz(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()