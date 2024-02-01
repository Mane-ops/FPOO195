"""def suma(*numeros):
    resultado = sum(numeros)
    print('suma', resultado)
suma(1,2,3,4)"""

import math

def area_cuadrado(lado):
    return lado**2

def main():
    lado_cuadrado=float(input('Ingrese valor del lado: '))
    area_result=area_cuadrado(lado_cuadrado)
    
    print(f"area del cuadrado: {area_result}")
    
main()