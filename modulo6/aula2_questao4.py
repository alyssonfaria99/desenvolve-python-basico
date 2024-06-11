tamanhoLista1 = int(input('Digite a quantidade de elementos da lista 1: '))
lista1 = []
for i in range(0,tamanhoLista1):
    lista1.append(int(input('Digite os 4 elementos da lista 1: ')))


tamanhoLista2 = int(input('Digite a quantidade de elementos da lista 2: '))
lista2 = []
for i in range(0,tamanhoLista2):
    lista2.append(int(input('Digite os 4 elementos da lista 2: ')))

listaAlternada = []

maiorTamanho = max(tamanhoLista1, tamanhoLista2)

for i in range(0, maiorTamanho):
    if i < tamanhoLista1:
        listaAlternada.append(lista1[i])
    if i < tamanhoLista2:
        listaAlternada.append(lista2[i])

    
print(listaAlternada)