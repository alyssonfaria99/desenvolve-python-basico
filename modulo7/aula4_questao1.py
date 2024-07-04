import os

frase = input('Digite uma frase: ')

with open('frase.txt','w') as f:
    f.write(frase)


name = os.path.abspath('frase.txt')
print(f'Frase salve em {name}')





