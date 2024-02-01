#muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
num = int(input('Ingresa un numero entero: '))
i = num
for i in range(num,-1,-1):
    print(i,end=", ")