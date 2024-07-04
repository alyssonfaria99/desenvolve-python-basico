with open('frase.txt','r+') as f:
    frase = f.read()
    palavras = frase.split(' ')
    for palavra in palavras:
        palavra = ''.join(letra if letra.isalpha() else '' for letra in palavra)
        with open('palavras.txt', 'a') as arquivoPalavras:
            arquivoPalavras.write(palavra + '\n')
    with open('palavras.txt','r') as resultado:
        print(resultado.read()) 


    

