import random

f = open('gabarito_forca.txt','r')

arrPalavras = f.readlines()
palavraAleatoria = arrPalavras[random.randint(0,9)]

f.close()

enforcado = open('gabarito_enforcado.txt','r')
arrStr = enforcado.readlines()
enforcado0 = arrStr[0:5]
enforcado1 =arrStr[6:11]
enforcado2 = arrStr[12:17]
enforcado3 = arrStr[18:23]
enforcado4 = arrStr[24:29]
enforcado5 = arrStr[30:35]
enforcado6 = arrStr[36:41]

arrEnforcados = [enforcado0,enforcado1, enforcado2, enforcado3, enforcado4, enforcado5, enforcado6]

palavraInicial = f'{len(palavraAleatoria) *  '_'}'
arrResposta = list(palavraAleatoria)
resultado = ['_' for i in range (0, len(palavraAleatoria) - 1)]

contador = 0
print(''.join(arrEnforcados[0]) + '\n')
print(''.join(resultado))

while contador < 7:
    palpite = input('Digite uma letra: ')
    if palpite in palavraAleatoria:
        for i in range (0, len(palavraInicial) - 1):
            if arrResposta[i] == palpite:
                print(''.join(arrEnforcados[contador]) + '\n')
                resultado[i] = palpite
        print(''.join(resultado))
        if (''.join(resultado) == palavraAleatoria[:-1]):
            print('Parabéns, você ganhou!!!')
            break
    else:
        contador += 1
        print(''.join(arrEnforcados[contador]) + '\n')
        print(''.join(resultado))
        if contador == 6:
            print('Você perdeu!')
            break
