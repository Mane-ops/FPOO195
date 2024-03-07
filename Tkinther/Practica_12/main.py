import sys
from Usuarios import *
from tkinter import *
from tkinter import messagebox

usuario = Usuarios()

while True:
    print("1. Registrar usuario ")
    print("2. Consultar solo un usuario ")
    print("3. Eliminar un usuario ")
    print("4. Editar un usuario ")
    print("5. Login")
    print("6. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        id= input("Escribe el Id: ")
        correo = input("Ingresa el correo: ")
        contrasena = input("Ingresa una contraseña: ")
        
        usuario.Registrar(id,correo,contrasena)
        print("Usuario registrado")

    elif opcion == "2":
        print("Ingresa el Id de algun usuario")
        id = input("Id: ")
        usuario.buscar(id)

    elif opcion == "3":
        print("Ingresa el Id de la persona a eliminar")
        id= input("Id: ")
        usuario.eliminar(id)

    elif opcion == "4":
        print("Ingresa el Id del usuario a editar")
        id = input("Id: ")
        cor = input("Nombre: ")
        con = input("Edad: ")
        usuario.editar(id,cor,con)
        
    elif opcion == "5":
        
        ventana = Tk()
        ventana.title("Login")
        ventana.geometry("700x500")
        
        seccion1 = Frame(ventana, bg = "#F4E900")
        seccion1.pack(expand=True, fill='both')
    
        seccion2 = Frame(ventana, bg = "#F4E900")
        seccion2.pack(expand=True, fill='both')
        
        seccion3 = Frame(ventana, bg = "#F4E900")
        seccion3.pack(expand=True, fill='both')  
    
        id = (Entry(seccion1))
        id.pack()
        cor = Entry(seccion1)
        cor.pack()
        cont = Entry(seccion2)  
        cont.grid(column=10, row=2)
        
        boton = Button(seccion3, text="Validar",bg="#090909", lambda: usuario.validarUsuario(id,cor,cont))
        boton.configure(height=2,width=10)
        boton.pack()
        
        

    elif opcion == "6":
        print("Adios")
        sys.exit()

    else:
        print("Opción no válida. Inténtalo de nuevo.")
        
    