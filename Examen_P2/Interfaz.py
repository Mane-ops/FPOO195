import tkinter as tk
from tkinter import messagebox
from Matricula import *

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
        self.boton.grid(row=5, column=0, columnspan=1, padx=10, pady=5)

        self.mat_entry = tk.Entry(self.root, width=30)
        self.mat_entry.grid(row=5, column=1, padx=10, pady=5)

    def matricula(self):
        try:
            an = self.linea_ann.get()
            no = self.linea_nom.get()
            ap = self.linea_app.get()
            am = self.linea_apm.get()
            ca = self.linea_ca.get()

            self.matricula_generador = Matricula(an,no,ap,am,ca)
            matri = self.matricula_generador.generador_matricula()

            messagebox.showinfo("Contraseña Generada", f"Su Matricula es: {matri}")
            self.mat_entry.delete(0, tk.END)
            self.mat_entry.insert(0, matri)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese una longitud válida.")

def main():
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()