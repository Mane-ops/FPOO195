class Persona:

#Constuctor

    def __init__(self):
        self.__listaBD = []

    #Metodos del CRUD

    def Insertar (self, id, nom, pasw):

        self.__listaBD.append(  {   "Id":id, "Nombre":nom, "Pasw":pasw }    )

    def consultarTodos (self):

        print(self.__listaBD)

    def buscarUsuario(self,id):
        for usuario in self.__listaBD:
            if usuario['Id'] == id:
                print( usuario)
            else:
                print("Usuario no encontrado")

    def eliminar(self, id):
        for usuario in self.__listaBD:
            if usuario['Id'] == id:
                self.__listaBD.remove(usuario)
                print(":: Usuario Eliminado::")
            
            self.consultarTodos()

    def editar(self, id, nom, pasw):
        for usuario in self.__listaBD:
            if usuario['Id'] == id:
                usuario ["Nombre"] = nom
                usuario['Pasw'] = pasw
                print(":: Usuario Editado::")

            self.consultarTodos()
            
    def validarUsuario(self, nombre,password):
        for usuario in self.__listaBD:
            if usuario['Nombre'] == nombre and usuario['Pasw'] == password :
                acesso = True
            else:
                acesso = False
            return acesso