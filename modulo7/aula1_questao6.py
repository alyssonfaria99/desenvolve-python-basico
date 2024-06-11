frase = input('Digite uma frase: ').lower()
palavrasDaFrase = frase.split(' ')
palavraObjetivo = input('Digite a palavra objetivo: ').lower()

anagramas = []

for palavra in palavrasDaFrase:
    if len(palavra) == len(palavraObjetivo):
        palavraOrdenada = sorted(palavra)
        palavraObjetivoOrdenada = sorted(palavraObjetivo)
        if palavraOrdenada == palavraObjetivoOrdenada:
            anagramas.append(palavra)

print(anagramas)


