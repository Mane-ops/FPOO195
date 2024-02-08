#Programa que solicita una palabra y lo descompone en letras
palabra = str(input('Ingresa una palabra: '))
x=1
for i in palabra:
    print(f'Letra {x}: {i}')
    x += 1