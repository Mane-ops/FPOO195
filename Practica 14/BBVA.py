class Usuario:
    def __init__(self):
        self.usuarios = {}

    def Insertar(self, id, nombre, edad, saldo):
        self.usuarios[id] = {'Nombre': nombre, 'Edad': edad, 'Saldo': saldo}

    def consultarTodos(self):
        return self.usuarios

    def buscarUsuario(self, id):
        return self.usuarios.get(id)

    def eliminar(self, id):
        if id in self.usuarios:
            del self.usuarios[id]
            return True
        else:
            return False

    def editar(self, id, nombre, edad, saldo):
        if id in self.usuarios:
            self.usuarios[id]['Nombre'] = nombre
            self.usuarios[id]['Edad'] = edad
            self.usuarios[id]['Saldo'] = saldo
            return True
        else:
            return False

    def consultarSaldo(self, id):
        if id in self.usuarios:
            return self.usuarios[id]['Saldo']
        else:
            return None

    def ingresarMonto(self, id, monto):
        if id in self.usuarios:
            self.usuarios[id]['Saldo'] += monto
            return True
        else:
            return False

    def retirarMonto(self, id, monto):
        if id in self.usuarios:
            if self.usuarios[id]['Saldo'] >= monto:
                self.usuarios[id]['Saldo'] -= monto
                return True
        return False

    def deposito(self, id_origen, monto, id_destino):
        if id_origen in self.usuarios and id_destino in self.usuarios:
            if self.usuarios[id_origen]['Saldo'] >= monto:
                self.usuarios[id_origen]['Saldo'] -= monto
                self.usuarios[id_destino]['Saldo'] += monto
                return True
        return False




