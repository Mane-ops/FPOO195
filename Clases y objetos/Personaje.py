class Personaje:
    
    #Atributos de personaje
    especie = "Humano"
    nombre = "John"
    altura = 2.18
    
    #Métodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje "+ self.nombre +" esta corriendo")
        else:
            print("El personaje "+ self.nombre +" esta muerto")
    
    def lanzarGranada(self):
        print(self.nombre+" Pego una granada")