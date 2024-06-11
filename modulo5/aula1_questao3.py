import random

numeroAlvo = random.randint(1,10)
numero = int
while numero != numeroAlvo:
    numero = int(input('Adivinhe o número: '))
    if (numero == numeroAlvo):
        print(f'Correto! o número é {numero}')
        break
    elif numero < numeroAlvo:
        print('Muito baixo, tente novamente!')
        continue
    else:
        print('Muito alto, tente novamente!')
        continue