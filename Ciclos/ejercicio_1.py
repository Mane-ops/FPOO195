#muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
num = int(input('Ingresa un numero entero: '))
for i in range(1,num+1):
    if i%2 != 0:
        print(i,end=", ")
        i+=1