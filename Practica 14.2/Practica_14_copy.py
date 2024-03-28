
class Usuario:
    def __init__(self):
        self.__listaBD = []

    def Insertar(self, cuenta, nombre, edad, saldo):
        self.__listaBD.append({"Cuenta": cuenta, "Titular": nombre, "Edad": edad, "Saldo": saldo})

    def consultarTodos(self):
        return self.__listaBD

    def buscarUsuario(self, cuen):
        for usuario in self.__listaBD:
            if usuario['Cuenta'] == cuen:
                return usuario
        return None

    def eliminar(self, cuen):
        for usuario in self.__listaBD:
            if usuario['Cuenta'] == cuen:
                self.__listaBD.remove(usuario)
                return True
        return False

    def editar(self, cuen, nom, ed, sal):
        for usuario in self.__listaBD:
            if usuario['Cuenta'] == cuen:
                usuario["Titular"] = nom
                usuario["Edad"] = ed
                usuario['Saldo'] = sal
                return True
        return False
    
    def consultarSaldo(self, cuen):
        for usuario in self.__listaBD:
            if usuario['Cuenta'] == cuen:
                return usuario['Saldo']
        return None
    
    def ingresarMonto(self, cuen, monto):
        for usuario in self.__listaBD:
            if usuario['Cuenta'] == cuen:
                usuario['Saldo'] += monto
                return usuario['Saldo'], True
        return False
    
    def RerirarMonto(self, cuen, monto):
        for usuario in self.__listaBD:
            if usuario['Cuenta'] == cuen:
                usuario['Saldo'] -= monto
                return usuario['Saldo'], True
        return False
    
    def deposito(self, cuen, monto, cuent):
        for usuario in self.__listaBD:
            if usuario['Cuenta'] == cuen:
                if monto<= usuario['Saldo']:
                    usuario['Saldo'] -= monto
                    for usuario2 in self.__listaBD:
                        if usuario2['Cuenta'] == cuent:
                            usuario2['Saldo'] += monto
                    return True
                return False
                        