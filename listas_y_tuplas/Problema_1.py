import statistics

n = int(input('Ingresa el tamaño de la tupla: '))
num = []
for i in range (n):
    x = int(input(f'Ingresa el numero {i+1}: '))
    num.append(x)
tupla = tuple(num)
print(tupla)

def suma():
    s = sum(tupla)
    print(f'Sumatoria: {s}')
    
def mayor():
    mx = max(tupla)
    print(f'Mayor: {mx}')
    
def menor():
    mn = min(tupla)
    print(f'Menor: {mn}')
    
def promedio():
    p = (sum(tupla))/len(tupla)
    print(f'Promedio: {p}')
    
def moda():
    m = statistics.mode(tupla)
    print(f'Moda: {m}')
    
def rango():
    r = (max(tupla))-(min(tupla))
    print(f'Rango: {r}')
    
suma()
mayor()
menor()
promedio()
moda()
rango()
