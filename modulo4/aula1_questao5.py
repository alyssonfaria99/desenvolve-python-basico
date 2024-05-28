n = int(input('Digite a quantidade de respondentes: '));
soma = 0
contador = 0

while n > contador:
    idade = int(input('Digite a idade: '))
    soma += idade
    contador += 1

media = soma / n
print(media)