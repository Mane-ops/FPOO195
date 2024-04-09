from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *
from tkinter import messagebox
from GeneradorPDF import *
import os

objControlador = Controlador()
objPDF = GeneradorPDF()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())
    
def busUsuario():
    usuarioBD = objControlador.buscarUsuario(varBus.get())
    if usuarioBD == []:
        messagebox.showwarning("Nada","Usuario no encontrado")
    else:
        resultado.delete(1.0, END)
        for i in usuarioBD:
            resultado.insert(END, f"ID: {i[0]}\nNombre: {i[1]}\nCorreo: {i[2]}\n")
        #resultado.insert(END, usuarioBD)

def ejecutaPDF():
    if varTitulo == " ":
        messagebox.showwarning("Importante","Escribe un nombre al PDF")
    else:
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(varTitulo.get()+".pdf")
        rutaPDF = "C:/Users/maner/OneDrive/Escritorio/POO/FPOO195/"+varTitulo.get()+".pdf"
        messagebox.showinfo("Archivo creado","PDF disponible en carpeta")
        os.system(f"start {rutaPDF}")

def busTodos():      
    for lista in tree.get_children():
        tree.delete(lista)
    for usuario in objControlador.consultarUsuarios():
        tree.insert("", "end",values=usuario)
        
# 1 Crear ventana
ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

# 2. preparar el notebook para pestañas
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand="yes")

# 3. Definir las pestañas del notebook
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)
pestana6 = ttk.Frame(panel)

# 4. agregamos las pestañas
panel.add(pestana1, text="Crear usuario")
panel.add(pestana2, text="Buscar usuario")
panel.add(pestana3, text="Consultar usuarios")
panel.add(pestana4, text="Editar usuario")
panel.add(pestana5, text="Eliminar usuario")
panel.add(pestana6, text="Exportar PDF")

# 5. Pestaña 1: Formulario de Insert
Label(pestana1, text="Registro de Usuarios", fg="blue", font=("Modern",18)).pack()

var1 = tk.StringVar()
Label(pestana1, text="Nombre: ").pack()
Entry(pestana1, textvariable=var1).pack()

var2 = tk.StringVar()
Label(pestana1, text="Correo: ").pack()
Entry(pestana1, textvariable=var2).pack()

var3 = tk.StringVar()
Label(pestana1, text="Contraseña: ").pack()
Entry(pestana1, textvariable=var3).pack()

Button(pestana1, text="Guardar usuario", command=ejecutaInsert).pack()

#6. Pestaña 2: Buscar Usuario
Label(pestana2, text="Buscar Usuarios", fg="red", font=("Mono",18)).pack()

varBus = tk.StringVar()
Label(pestana2, text="ID: ").pack()
Entry(pestana2, textvariable=varBus).pack()

Button(pestana2, text="Buscar Usuario", command=busUsuario).pack()

Label(pestana2, text="Usuario encontrado: ", fg="blue", font=("Mono", 16)).pack()
resultado = tk.Text(pestana2, height=5, width=52)
resultado.pack()

#7. Pestaña 3: Consultar usuarios
tree = ttk.Treeview(pestana3, columns=("ID", "Nombre", "Correo"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Correo", text="Correo")
tree.pack(fill="both", expand=True)
Button(pestana3, text="Consultar Todos los Usuarios", command=busTodos).pack()



# Pestaña 6: Exportar PDF
Label(pestana6, text="Usuario en PDF", fg="green", font=("Modern",18)).pack()
varTitulo = tk.StringVar()
Label(pestana6, text="Escribe el título de tu archivo: ").pack()
Entry(pestana6, textvariable=varTitulo).pack()

Button(pestana6, text="Crear PDF", command=ejecutaPDF).pack()




ventana.mainloop()