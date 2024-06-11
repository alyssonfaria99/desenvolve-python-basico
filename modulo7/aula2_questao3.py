frase = ''

while frase != 'fim':
    frase = input('Digite uma frase (digite "fim" para encerrar):')
    fraseFormatada = frase.lower().replace(' ','')
    for caracter in fraseFormatada:
        if not caracter.isalnum():
            fraseFormatada = fraseFormatada.replace(caracter, '')

    fraseInvertida = fraseFormatada[::-1]
    if fraseFormatada == fraseInvertida:
        print('"'+frase +'"'  ' é palíndromo.')
    else:
        print('Não é palídromo.')