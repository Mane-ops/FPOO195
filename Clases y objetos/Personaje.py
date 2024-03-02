class Personaje:
    
    #Atributos de personaje
    
    def __init__(self, esp, nom, alt):
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
        
        
    def getEspecie(self):
        return self.__especie
    
    def getNombre(self):
        return self.__nombre
    
    def getAltura(self):
        return self.__altura
    
    def setEspecie(self, ex):
        self.__especie = ex
    
    def setNombre(self, nx):
        self.__nombre = nx
    
    def setAltura(self, ax):
        self.__altura = ax
    
    #Métodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje "+ self.__nombre +" esta corriendo")
        else:
            print("El personaje "+ self.__nombre +" esta muerto")
    
    def __pensar(self):
        print(self.__)
    
    def lanzarGranada(self):
        print(self.__nombre+" Pego una granada")
        