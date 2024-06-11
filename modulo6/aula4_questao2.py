frase = input('Digite uma frase: ')

vogais = ['a','e','i','o','u']

vogaisNaFrase = [ n for n in frase.lower() if n in vogais]
consoantesNaFrase = [ n for n in frase.lower() if (not (n in vogais) and n != ' ')]

print(sorted(vogaisNaFrase))
print(consoantesNaFrase)