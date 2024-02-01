#Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
cuenta = 0
print ("Escriba una bitacora de operaciones bancarias: ")
while True:
    movimiento = input()
    if not movimiento:
        break
    #split sirve para separar los datos y no tomar en cuenta el espacio en blanco
    x = movimiento.split(" ")
    #guarda los valores en un "arreglo" para tomar sus posiciones como valores separados
    op = x[0]
    cantidad = int(x[1])
    if op=="D":
        cuenta+=cantidad
    elif op=="R":
        cuenta-=cantidad
    else:
        #pass sirve para señalar si no hay ninguna operación y darle la señal al bucle para que realice el break ya que no hay movimientos
        pass
print (cuenta)