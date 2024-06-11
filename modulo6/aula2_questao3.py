import random

lista1 = [random.randint(0,50) for i in range(0,20)]
lista2 = [random.randint(0,50) for i in range(0,20)]
lista3 = []

for i in lista1:
    if (i in lista2 and (not i in lista3)):
        lista3.append(i)

print(lista3)

listaInterseccaoOrdenada = sorted(lista3)
print(listaInterseccaoOrdenada)

print('Contagem')
for i in listaInterseccaoOrdenada:
    print(f'{i}:(lista 1={lista1.count(i)}, lista2={lista2.count(i)})')


