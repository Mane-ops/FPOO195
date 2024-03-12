from tkinter import Tk, Frame, Button, Label, messagebox, Entry
import tkinter as tk

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
