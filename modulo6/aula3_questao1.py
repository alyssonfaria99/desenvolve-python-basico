tamanhoLista = int(input('Digite o tamanho da lista (pelo menos 4): '))
lista = []

if tamanhoLista < 4:
    print('A lista deve conter pelo menos 4 elementos')
else :
    for i in range(0, tamanhoLista):
        lista.append(int(input('Digite um valor da lista: ')))
print (lista)

print(lista[:3])
print(lista[-2:tamanhoLista])
print(lista[::-1])
print(lista[::2])
print(lista[1::2])