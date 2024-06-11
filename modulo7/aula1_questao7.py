import random

nomes_crypt = []

def encrypt(listaStr):
    valorAleatorio = random.randint(1,10)
    for str in listaStr:
        novaPalavra = ''
        for letra in str:
            unicode = ord(letra)
            novaLetra = chr(unicode + valorAleatorio)
            novaPalavra += novaLetra
         
        nomes_crypt.append(novaPalavra)

    print (f'chave_aleatoria = {valorAleatorio}\n{nomes_crypt}')

encrypt(["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"])
