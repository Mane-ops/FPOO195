frase = str(input('Introduce una palabra: '))
pal = frase[::-1]
if frase==pal:
    print('La palabra es un palindromo')
else:
    print('La palabra no es un palindromo')