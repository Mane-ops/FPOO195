from tkinter import messagebox
class Usuarios:
    def __init__(self):
        self.__usuarios = []

    def Registrar (self, id, co, passw):

        self.__usuarios.append({"Id":id, "Correo":co, "Contrasena":passw })

    def buscar(self,id):
        for i in self.__usuarios:
            if i['Id'] == id:
                print(i)
            else:
                print("Usuario no encontrado")

    def eliminar(self, id):
        for i in self.__usuarios:
            if i['Id'] == id:
                self.__usuarios.remove(i)
                print("Usuario eliminado")
            

    def editar(self, id, co, passw):
        for i in self.__usuarios:
            if i ['Id'] == id:
                i ["Correo"] = co
                i['Contraseña'] = passw
                print("Usuario editado")
                
    def validarUsuario(self, co, passw):
        for i in self.__usuarios:
            if i ['Correo'] == co:
                if i ['Contrasena'] == passw:
                    print(messagebox.showinfo('Info', 'Acceso permitido'))
                else:
                    print(messagebox.showerror('ERROR', 'Revisa tus credenciales'))