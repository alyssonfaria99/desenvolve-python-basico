import random

def embaralhar_palavras(frase):
    palavras = frase.split(' ')
    print(palavras)
    resultado = ''
    for palavra in palavras:
        letras = list(palavra)
        primeiraLetra = letras[0]
        ultimaLetra = letras[len(letras) - 1]
        letrasDoMeio = letras[1:len(letras) - 1]
        random.shuffle(letrasDoMeio)
        palavraEmbaralhada = primeiraLetra + ''.join(letrasDoMeio) + ultimaLetra
        resultado += ' ' + palavraEmbaralhada
    print(resultado)

embaralhar_palavras('Atletico Mineiro Galo Doido')