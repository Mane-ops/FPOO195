"""Escribir una función que calcule el total de una factura tras aplicarle
el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de
IVA a aplicar, y devolver el total de la factura. Si se invoca la función
sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""

def pago():
    cantidad = float(input('Introduzca la cantidad sin IVA: '))
    iva = float(input('Ingresa el porcentaje de IVA que se aplicará a la cantidad: ')or 21)
    iva = iva/100
    cantidad = cantidad + (cantidad*iva)
    print(f'La cantidad con iva es de {cantidad}')

pago()