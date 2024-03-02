class Usuario:
    usuarios = []

    def _init_(self, nom, corr, pas):
        self.__nombre = nom
        self.__correo = corr
        self.__password = pas
        Usuario.usuarios.append(self)

    def agregar(self):
        print("Usuario agregado:")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")
        print(f"Contraseña: {self.__password}")

    def consultar(self):
        print("Información del usuario:")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")

    def editar(self, nom, corr, pas):
        self.__nombre = nom
        self.__correo = corr
        self.__password = pas
        print("Usuario editado.")

    def eliminar(self):
        Usuario.usuarios.remove(self)
        print("Usuario eliminado exitosamente.")

    def getNombre(self):
        return self.__nombre

    def getCorreo(self):
        return self.__correo

    def getPassword(self):
        return self.__password

    def setNombre(self, nx):
        self.__nombre = nx

    def setCorreo(self, cx):
        self.__correo = cx

    def setPassword(self, px):
        self.__password = px