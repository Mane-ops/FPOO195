import random

def lista_random():
    return [random.randint(10, 20) for _ in range (30)]

lista = lista_random()

def rep(lista):
    return {num : lista.count(num) for num in set(lista)}

def elim(lista):
    return list(set(lista))

def rem(lista):
    for num in set(lista):
        while lista.count(num) > 1:
            lista[lista.index(num)] = 0
    return lista

x = str(input('Elija una opcion:\n a) Contar número repetidos\n b) Eliminar numero repetidos\n c) Remplazar los repetidos con 0\n'))

if x == 'a':
    print(rep(lista))
elif x == 'b':
    print(elim(lista))
elif x == 'c':
    print(rem(lista))

print(f'La lista original es: {lista}')

