"""Escribir una función que convierta un número decimal en binario y
otra que convierta un número binario en decimal."""

decimal = int(input('Introduce un numero en decimal: '))
binario = int(input('Introduce un numero en binario: '))
def bin_dec():
    b = bin(decimal)
    print(f'El numero decimal convertido a binario es {b}')
    
def dec_bin():
    d = int(str(binario),2)
    print(f'El numero binario ingresado en valor decimal es: {d}')

bin_dec()
dec_bin()