def pago():
    cantidad = float(input('Introduzca la cantidad sin IVA: '))
    iva = float(input('Ingresa el porcentaje de IVA que se aplicará a la cantidad: ')or 21)
    iva = iva/100
    cantidad = cantidad + (cantidad*iva)
    print(f'La cantidad con iva es de {cantidad}')

pago()