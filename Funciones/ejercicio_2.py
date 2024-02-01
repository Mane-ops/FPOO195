import math
def area_circulo(r):
    return math.pi*(math.pow(r,2))

def area_cilindro(r,h):
    return area_circulo(r)*h

radio = float(input('ingresa el valor del radio: '))
altura = float(input('ingresa el valor de la altura: '))

print(area_circulo(radio))
print(area_cilindro(radio,altura))