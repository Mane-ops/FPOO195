import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Persona:
    def __init__(self):
        self.__listaBD = []

    def Insertar(self, id, nom, pasw):
        self.__listaBD.append({"Id": id, "Nombre": nom, "Pasw": pasw})

    def consultarTodos(self):
        return self.__listaBD

    def buscarUsuario(self, id):
        for usuario in self.__listaBD:
            if usuario['Id'] == id:
                return usuario
        return None

    def eliminar(self, id):
        for usuario in self.__listaBD:
            if usuario['Id'] == id:
                self.__listaBD.remove(usuario)
                return True
        return False

    def editar(self, id, nom, pasw):
        for usuario in self.__listaBD:
            if usuario['Id'] == id:
                usuario["Nombre"] = nom
                usuario['Pasw'] = pasw
                return True
        return False


class Interfaz(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Gestión de Usuarios")

        self.persona = Persona()

        # Crear widgets
        self.label_id = tk.Label(self, text="ID:")
        self.entry_id = tk.Entry(self)
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.entry_nombre = tk.Entry(self)
        self.label_password = tk.Label(self, text="Contraseña:")
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
        self.label_password.grid(row=2, column=0)
        self.entry_password.grid(row=2, column=1)
        self.button_insertar.grid(row=3, column=0)
        self.button_consultar_todos.grid(row=3, column=1)
        self.button_buscar.grid(row=4, column=0)
        self.button_eliminar.grid(row=4, column=1)
        self.button_editar.grid(row=5, column=0)
        self.text_output.grid(row=6, columnspan=2)

    def insertar_usuario(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        password = self.entry_password.get()
        self.persona.Insertar(id, nombre, password)
        self.text_output.insert(tk.END, f"Usuario insertado: {id}, {nombre}, {password}\n")

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
            self.text_output.insert(tk.END, f"Usuario con ID {id} eliminado\n")
        else:
            self.text_output.insert(tk.END, f"No se encontró usuario con ID {id}\n")

    def editar_usuario(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        password = self.entry_password.get()
        if self.persona.editar(id, nombre, password):
            self.text_output.insert(tk.END, f"Usuario con ID {id} editado\n")
        else:
            self.text_output.insert(tk.END, f"No se encontró usuario con ID {id}\n")

if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()
    
class Login:
    def crearLogin(self, objPeople):
        def ejecutaValidacion():
            status= objPeople.validarUsuario(var1.get(), var2.get())
            if(status):
                print(messagebox.showinfo('Bienvenido', 'Acesso Concedido'))
            else:
                print(messagebox.showerror('Error', 'Usuario no encontrado'))

        Ventana = Tk()
        Ventana.title("Login Persona")
        Ventana.geometry("600x400")
        seccion1= Frame(Ventana)
        seccion1.pack(expand= True, fill='both')
        Label(seccion1, text="Login FPOO", bg="black", fg="white", font=("Mono", 18)).pack()
        var1= tk.StringVar()
        Label(seccion1, text="Usuario:", font=("Helvetica", 14)).pack()
        Entry(seccion1, takefocus= True, textvariable = var1).pack()
        var2= tk.StringVar()
        Label(seccion1, text="Contraseña:", font=("Helvetica",14)).pack()
        Entry(seccion1, show="+", textvariable= var2).pack()
        botonAcesso= Button(seccion1, text="Acceder", command= ejecutaValidacion)
        botonAcesso.pack()
        Ventana.mainloop()