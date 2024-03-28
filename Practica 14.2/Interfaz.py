import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Practica_14_copy import *
from Interfaz2 import *


class Interfaz1(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Gestión de Usuarios")

        self.persona = Usuario()

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
        self.text_output.grid(row=8, columnspan=2)

    def insertar_usuario(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        saldo = float(self.entry_password.get())
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
            print(messagebox.showinfo("Usuario encontrado",f"{usuario}\n"))
        else:
            print(messagebox.showerror("Error",f"Cuenta {id} no encontrada\n"))

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

    
    
class Interfaz2(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Gestión de Usuarios")

        self.persona = Usuario()

        # Crear widgets
        self.label_id = tk.Label(self, text="No. Cuenta:")
        self.entry_id = tk.Entry(self)
        self.label_monto = tk.Label(self, text="Monto:")
        self.entry_monto = tk.Entry(self)
        self.label_id2 = tk.Label(self, text="No. Cuenta destino:")
        self.entry_id2 = tk.Entry(self)
        self.button_saldo = tk.Button(self, text="Consultar saldo", command=self.consulta_saldo)
        self.button_ingrsar = tk.Button(self, text="Depositar dinero", command=self.depositar_monto)
        self.button_retirar = tk.Button(self, text="Retirar dinero", command=self.retirar_monto)
        self.button_depositar = tk.Button(self, text="Realizar depósito", command=self.depositar)
        self.text_output = tk.Text(self, height=10, width=50)

        # Posicionar widgets en la ventana
        self.label_id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)
        self.label_monto.grid(row=1, column=0)
        self.entry_monto.grid(row=1, column=1)
        self.label_id2.grid(row=2, column=0)
        self.entry_id2.grid(row=2, column=1)
        self.button_saldo.grid(row=4, column=0)
        self.button_ingrsar.grid(row=4, column=1)
        self.button_retirar.grid(row=5, column=0)
        self.button_depositar.grid(row=5, column=1)
        self.text_output.grid(row=7, columnspan=2)

    def consulta_saldo(self):
        id = self.entry_id.get()
        usuario = self.persona.consultarSaldo(id)
        if usuario:
            self.text_output.insert(tk.END, f"Saldo de la cuenta {id}\n {usuario}\n")
        else:
            print(messagebox.showerror("Error",f"Cuenta {id} no encontrada\n"))

    def depositar_monto(self):
        id = self.entry_id.get()
        monto = float(self.entry_monto.get())
        if self.persona.ingresarMonto(id, monto):
            usuario = self.persona.consultarSaldo(id)
            self.text_output.insert(tk.END, f"Nuevo saldo de la cuenta {id}\n {usuario}")
        else: 
            print(messagebox.showerror("Error",f"Cuenta {id} no encontrada\n"))
            
    def retirar_monto(self):
        id = self.entry_id.get()
        monto = float(self.entry_monto.get())
        if self.persona.RerirarMonto(id, monto):
            usuario = self.persona.consultarSaldo(id)
            self.text_output.insert(tk.END, f"Nuevo saldo de la cuenta {id}\n {usuario}")
        else: 
            print(messagebox.showerror("Error",f"Cuenta {id} no encontrada\n"))
            
    def depositar(self):
        id = self.entry_id.get()
        id2 = self.entry_id2.get()
        monto = float(self.entry_monto.get())
        if self.persona.deposito(id, monto, id2):
            print(messagebox.showinfo("Deposito realizado","Se realizó el depósito de manera correcta\n"))
        else:
            print(messagebox.showerror("Error","Revisa las credenciales\n"))    

if __name__ == "__main__":
    gestor_usuarios = Usuario()
    app1 = Interfaz1(gestor_usuarios)
    app1.mainloop()
    app2 = Interfaz2(gestor_usuarios)
    app2.mainloop()