import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Practica_14_copy import *

class Interfaz2(tk.Tk):
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
            self.text_output.insert(tk.END, f"Saldo de la cuenta {id}\n {usuario}")
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
    app = Interfaz2()
    app.mainloop()