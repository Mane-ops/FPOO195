from Personaje import *
from Armas import *

#Solicitar datos de spartan
print("===== Datos de Heroe =====")
nombreS = input("Escribe el nombre de tu Spartan ")
especieS = input("Escribe la especie de tu Spartan ")
alturaS = float(input("Escribe la altura de tu Spartan "))
print("")

#Solicitar datos de Nemesis
print("===== Datos de Villano =====")
nombreN = input("Escribe el nombre de tu Nemesis ")
especieN = input("Escribe la especie de tu Nemesis ")
alturaN = float(input("Escribe la altura de tu Nemesis "))
print("")

#creamos el objeto de la clase personaje
spartan = Personaje(especieS,nombreS,alturaS)
Nemesis = Personaje(especieN,nombreN,alturaN)
Arma = Armas()

#usamos los atributos spartan
print("===== El objeto Spartan contiene =====")
print(spartan.getNombre())
print(spartan.getEspecie())
print(spartan.getAltura())
print("")

#usamos los atributos nemesis
print("===== El objeto Nemesis contiene =====")
print(Nemesis.getNombre())
print(Nemesis.getEspecie())
print(Nemesis.getAltura())
print("")

#Usamos los metodos del spartan
spartan.correr(True)
spartan.lanzarGranada()
print("")

#Usamos los metodos del nemesis
Nemesis.correr(False)
Nemesis.lanzarGranada()
print("")

#Usamos los metodos del arma
Arma.seleccionarArma(spartan.getNombre())
Arma.recargarArma(65)