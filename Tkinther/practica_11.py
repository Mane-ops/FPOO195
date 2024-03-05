from tkinter import Tk, Frame, Button, messagebox

#Metodo para mensaje
def mostrarMensajes():
    print(messagebox.showinfo('Showinfo', 'Information'))
    print(messagebox.showerror('Showerror', 'Error'))
    print(messagebox.showwarning('Showwarning', 'Warning'))
    print(messagebox.askokcancel(message="¿Desea continuar?", title="Soy el título"))
    
    
#Metodo 

def addbtn():
    botonVerde.config(text="+")
    botonRosa = Button(seccion3,text="Nuevo",bg="#f7089c")
    botonRosa.configure(height=3,width=5)
    botonRosa.pack()

#1. Creamos la ventana
Ventana = Tk() #Uso de POO creando un objeto Ventana
Ventana.title("Ejemplo con 3 Frames")
Ventana.geometry("600x400")

#2. Colocamos Frames de la ventana
seccion1 = Frame(Ventana, bg = "red")
seccion1.pack(expand=True, fill='both')

seccion2 = Frame(Ventana, bg = "#F4E900")
seccion2.pack(expand=True, fill='both')

seccion3 = Frame(Ventana, bg = "#0C72FD")
seccion3.pack(expand=True, fill='both')

#3. Posicionar Botones

#place
botonAzul = Button(seccion1,text="Azul", fg="#0733f7")
botonAzul.place(x=60, y=60, width=100, height=30)

#grid
botonNegro = Button(seccion2,text="Negro",fg="#FFFFFF" ,bg="#090909")
#siempre se usa un configure cuando se usa grid
botonNegro.configure(height=2,width=10)
botonNegro.grid(row=0,column=1)

botonAmarillo = Button(seccion2,text="amarillo",bg="#fbff00", command=mostrarMensajes)
#siempre se usa un configure cuando se usa grid
botonAmarillo.configure(height=2,width=10)
botonAmarillo.grid(row=1,column=1)

botonVerde = Button(seccion3,text="Verde",bg="#06e813", command=addbtn)
botonVerde.configure(height=2,width=10)
botonVerde.pack()

botonVerde2= Button(seccion3,text="Verde2",bg="#06e813")
botonVerde2.configure(height=2,width=10)
botonVerde2.pack()

#Ejecuta la ventana
Ventana.mainloop()