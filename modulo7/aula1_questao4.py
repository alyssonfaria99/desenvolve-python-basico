numero = input('Digite o número: ')

if len(numero) < 9 :
    numero = '9' + numero

if (numero[0] != '9' and len(numero) == 9):
    print('O primeiro dígito deve ser 9')
else:
    primeiraParte = numero[:5]
    segundaParte = numero[5:len(numero)]


    print('Numero completo:', primeiraParte + '-' + segundaParte)