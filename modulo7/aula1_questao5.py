frase = input('Digite uma frase: ')

contadorDeVogais = 0
indices = []

for letra in 'aeiou':
    for i in range (0, len(frase)):
        if letra == frase[i]:
            contadorDeVogais += 1
            indices.append(i)

indicesOrdenados = sorted(indices)

print('Vogais:', contadorDeVogais)
print(indicesOrdenados)