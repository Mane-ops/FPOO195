import tkinter as tk
from serie import Serie

class Interfaz:
    def __init__(self, master):
        self.master = master
        master.title("Serie")

        self.titulo_label = tk.Label(master, text="Título:")
        self.titulo_label.pack()

        self.titulo_entry = tk.Entry(master)
        self.titulo_entry.pack()

        self.genero_label = tk.Label(master, text="Género:")
        self.genero_label.pack()

        self.genero_entry = tk.Entry(master)
        self.genero_entry.pack()

        self.reproducir_button = tk.Button(master, text="Reproducir", command=self.reproducir)
        self.reproducir_button.pack()

        self.agregar_button = tk.Button(master, text="Agregar a mi lista", command=self.agregar_a_lista)
        self.agregar_button.pack()

        self.completada_button = tk.Button(master, text="Marcar como completada", command=self.marcar_como_completada)
        self.completada_button.pack()

        self.calificar_button = tk.Button(master, text="Calificar", command=self.calificar)
        self.calificar_button.pack()

    def reproducir(self):
        titulo = self.titulo_entry.get()
        genero = self.genero_entry.get()
        serie = Serie(titulo, genero)
        resultado = serie.reproducir()
        print(resultado)

    def agregar_a_lista(self):
        titulo = self.titulo_entry.get()
        genero = self.genero_entry.get()
        serie = Serie(titulo, genero)
        resultado = serie.agregar_a_lista()
        print(resultado)

    def marcar_como_completada(self):
        titulo = self.titulo_entry.get()
        genero = self.genero_entry.get()
        serie = Serie(titulo, genero)
        serie.marcar_como_completada()
        print(f"{titulo} marcada como completada")

    def calificar(self):
        titulo = self.titulo_entry.get()
        genero = self.genero_entry.get()
        serie = Serie(titulo, genero)
        calificacion = input("Ingrese la calificación: ")
        serie.calificar(calificacion)
        print(f"{titulo} calificada con {calificacion}")

root = tk.Tk()
app = Interfaz(root)
root.mainloop()
