class Personaje:
    
    #Atributos de personaje
    especie = "Humano"
    nombre = "John"
    altura = 2.18
    
    #Métodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje esta corriendo"+ self.nombre +" esta corriendo")
        else:
            print("El personaje esta corriendo"+ self.nombre +" esta muerto")
    
    def lanzarGranada(self):
        print(self.nombre+" Pego una granada")
    
    def recargarArma(self, municion):
        cargador = 25
        cargador = cargador + municion
        print("arma recargada al "+ str(cargador)+ "%")

#creamos el objeto de la clase personaje
spartan = Personaje()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)