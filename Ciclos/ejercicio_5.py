#programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
palabra = str(input('Introduce una palabra: '))
letra = str(input('Introduce una letra: '))
contador = 0
for x in palabra:
    if x == letra:
        contador += 1
print(f'La palabra {palabra} tiene {contador} letras {letra}')