base = int(input("Ingrese la cantidad de bases del arbol: "))
y = base - 1
x = 1

while y >= 0:
    print(' ' * y + '*' * x + ' ' * y)
    x+=2
    y-=1