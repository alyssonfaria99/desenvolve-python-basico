import random
import math

n = int(input('Número de valores: '))
soma = 0
for i in range(0, n):
    numero = random.randint(0,100)
    soma += numero

raiz = math.sqrt(soma)
print(raiz)