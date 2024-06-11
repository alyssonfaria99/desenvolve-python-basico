import random

lista = [random.randint(-10,10) for i in range(0,20)]

print(lista)

negativosAtual = 0
maxNegativos = 0

for i in range ( 0, len(lista)):
    if lista[i] < 0:
        negativosAtual +=1
        if negativosAtual > maxNegativos:
            maxNegativos = negativosAtual
            ultimoIndice = i
    else:
        negativosAtual = 0

primeiroIndice = ultimoIndice - maxNegativos + 1

del lista [primeiroIndice:ultimoIndice + 1]

print(lista)