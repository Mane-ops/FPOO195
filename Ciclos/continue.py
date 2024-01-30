contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(contador)
else:
    print('el bucle ha terminado normalmente')