#Programa que genera la serie de Collatz
num = int(input('Introduce un numero entero: '))
while num > 1 :
    if num%2 == 0:
        num = num/2
    elif num%2 != 0:
        num = (num*3)+1
    print(num)