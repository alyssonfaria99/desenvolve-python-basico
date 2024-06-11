import random

arr = []
for i in range(0, 20):
    x = random.randint(-100,100)
    arr.append(x)

listaOrdenada = sorted(arr)
print(listaOrdenada)
print(arr)
print(arr.index(max(arr)))
print(arr.index(min(arr)))
