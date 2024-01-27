edad = int(input('Introduce tu edad para darte el precio: '))
if edad<4:
    print('Entras gratis')
elif edad>=4 and edad<=18:
    print('Tu precio de entrada es de $110')
else:
    print('Tu precio de entrada es de $190')