class Personaje:
    
    #Atributos de personaje
    
    def __init__(self, esp, nom, alt):
        self.especie = esp
        self.nombre = nom
        self.altura = alt
    
    #Métodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje "+ self.nombre +" esta corriendo")
        else:
            print("El personaje "+ self.nombre +" esta muerto")
    
    def lanzarGranada(self):
        print(self.nombre+" Pego una granada")