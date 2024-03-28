import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Persona:
    def __init__(self):
        self.__listaBD = []

    def Insertar(self, cuenta, nombre, edad, saldo):
        self.__listaBD.append({"Cuenta": cuenta, "Titular": nombre, "Edad": edad, "Saldo": saldo})

    def consultarTodos(self):
        return self.__listaBD

    def buscarUsuario(self, cuen):
        for usuario in self.__listaBD:
            if usuario['Cuenta'] == cuen:
                return usuario
        return None

    def eliminar(self, cuen):
        for usuario in self.__listaBD:
            if usuario['Cuenta'] == cuen:
                self.__listaBD.remove(usuario)
                return True
        return False

    def editar(self, cuen, nom, ed, sal):
        for usuario in self.__listaBD:
            if usuario['Cuenta'] == cuen:
                usuario["Titular"] = nom
                usuario["Edad"] = ed
                usuario['Saldo'] = sal
                return True
        return False


class Interfaz(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Gestión de Usuarios")

        self.persona = Persona()

        # Crear widgets
        self.label_id = tk.Label(self, text="No. Cuenta:")
        self.entry_id = tk.Entry(self)
        self.label_nombre = tk.Label(self, text="Titular:")
        self.entry_nombre = tk.Entry(self)
        self.label_edad = tk.Label(self, text="Edad:")
        self.entry_edad = tk.Entry(self)
        self.label_password = tk.Label(self, text="Saldo:")
        self.entry_password = tk.Entry(self)
        self.button_insertar = tk.Button(self, text="Insertar", command=self.insertar_usuario)
        self.button_consultar_todos = tk.Button(self, text="Consultar Todos", command=self.consultar_todos)
        self.button_buscar = tk.Button(self, text="Buscar", command=self.buscar_usuario)
        self.button_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_usuario)
        self.button_editar = tk.Button(self, text="Editar", command=self.editar_usuario)
        self.text_output = tk.Text(self, height=10, width=50)

        # Posicionar widgets en la ventana
        self.label_id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)
        self.label_nombre.grid(row=1, column=0)
        self.entry_nombre.grid(row=1, column=1)
        self.label_edad.grid(row=2, column=0)
        self.entry_edad.grid(row=2, column=1)
        self.label_password.grid(row=3, column=0)
        self.entry_password.grid(row=3, column=1)
        self.button_insertar.grid(row=4, column=0)
        self.button_consultar_todos.grid(row=4, column=1)
        self.button_buscar.grid(row=5, column=0)
        self.button_eliminar.grid(row=5, column=1)
        self.button_editar.grid(row=6, column=0)
        self.text_output.grid(row=7, columnspan=2)

    def insertar_usuario(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        saldo = self.entry_password.get()
        self.persona.Insertar(id,nombre,edad,saldo)
        self.text_output.insert(tk.END, f"Usuario registrado: {id}, {nombre}, {edad}, {saldo}\n")

    def consultar_todos(self):
        usuarios = self.persona.consultarTodos()
        self.text_output.insert(tk.END, "Usuarios:\n")
        for usuario in usuarios:
            self.text_output.insert(tk.END, f"{usuario}\n")

    def buscar_usuario(self):
        id = self.entry_id.get()
        usuario = self.persona.buscarUsuario(id)
        if usuario:
            self.text_output.insert(tk.END, f"Usuario encontrado: {usuario}\n")
        else:
            self.text_output.insert(tk.END, "Usuario no encontrado\n")

    def eliminar_usuario(self):
        id = self.entry_id.get()
        if self.persona.eliminar(id):
            self.text_output.insert(tk.END, f"Cuenta {id} eliminada\n")
        else:
            self.text_output.insert(tk.END, f"No se encontró la cuenta {id}\n")

    def editar_usuario(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        password = self.entry_password.get()
        if self.persona.editar(id, nombre, password):
            self.text_output.insert(tk.END, f"Cuenta {id} editado\n")
        else:
            self.text_output.insert(tk.END, f"No se encontró la cuenta {id}\n")

if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()