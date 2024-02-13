import random
import collections

nums = []
for i in range(30):
    num = random.randrange(10,20)
    nums.append(num)
tupla = tuple(nums)

x = str(input('Selecciona una accion para realizar: \n a) Contar número repetidos\n b) Eliminar numero repetidos \n c) Remplazar los repetidos con 0\n'))


def repe():
    r = collections.Counter(tupla)
    print(r)

def elim():
    e = (set(tupla))
    print(e)
    
def rem():
    for i in set(tupla):
        while tupla.count(i) > 1:
            tupla[tupla.index(i)] = 0 
    return tupla         

print(tupla)
repe()
elim()
rem(tupla)