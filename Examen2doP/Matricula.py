import random
import string
import tkinter as tk
from tkinter import messagebox

class Matricula:
    def __init__(self, nacimiento = "", nombre = "", apep = "", apem = "", carrera = ""):
        self.curso = 2024
        self.nacimiento = nacimiento
        self.nombre = nombre
        self.apep = apep
        self.apem = apem
        self.carrera = carrera
        
    
    def generador_matricula(self):
        
        cur = self.curso[:2]
        nac = self.nacimiento[:2]
        nom = self.nombre[:1]
        apep = self.apep[:1]
        apem = self.apem[:1]
        aleatorio = random(string.digits)
        carr = self.carrera[:3]
        
        mat = (cur + nac + nom.upper() + apep.upper() + apem.upper() + aleatorio + aleatorio + aleatorio + carr.upper())
        
        return str(mat)
        
class Interfaz:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Matricula")
        
        obj = Matricula()
        self.widgets()
        
    def widgets(self):
        self.ann = tk.Label(self.root, text="Año de nacimiento:")
        self.ann.grid(row=0, column=0, padx=10, pady=5)
        
        self.linea_ann = tk.Entry(self.root)
        self.linea_ann.grid(row=0, column=1, padx=10, pady=5)
        
        self.nom = tk.Label(self.root, text="Nombre:")
        self.nom.grid(row=1, column=0, padx=10, pady=5)
        
        self.linea_nom = tk.Entry(self.root)
        self.linea_nom.grid(row=1, column=1, padx=10, pady=5)

        self.app = tk.Label(self.root, text="Apellido Paterno:")
        self.app.grid(row=2, column=0, padx=10, pady=5)
        
        self.linea_app = tk.Entry(self.root)
        self.linea_app.grid(row=2, column=1, padx=10, pady=5)
        
        self.apm = tk.Label(self.root, text="Apellido Materno:")
        self.apm.grid(row=3, column=0, padx=10, pady=5)
        
        self.linea_apm = tk.Entry(self.root)
        self.linea_apm.grid(row=3, column=1, padx=10, pady=5)
        
        self.ca = tk.Label(self.root, text="Carrera:")
        self.ca.grid(row=4, column=0, padx=10, pady=5)
        
        self.linea_ca = tk.Entry(self.root)
        self.linea_ca.grid(row=4, column=1, padx=10, pady=5)
        
        self.boton = tk.Button(self.root, text="Generar Matricula", command=self.matricula)
        self.boton.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.password_entry = tk.Entry(self.root, width=30)
        self.password_entry.grid(row=5, column=1, padx=10, pady=5)

    def matricula(self):
        try:
            an = int(self.linea_ann.get())
            no = self.linea_nom.get()
            ap = self.linea_app.get()
            am = self.linea_apm.get()
            ca = self.linea_ca.get()

            self.matricula_generador = Matricula(an,no,ap,am,ca)
            matri = self.matricula_generador.generador_matricula()

            messagebox.showinfo("Contraseña Generada", f"Su contraseña es: {matri}")
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, matri)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese una longitud válida.")

def main():
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()