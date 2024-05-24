distancia = int(input('Distância da entrega (km): '))
peso = int(input('Peso do pacote (kg): '))

if distancia <= 100:
    valorPorKg = 1
elif distancia <= 300:
    valorPorKg = 1.5
else:
    valorPorKg = 2

valorTotal = valorPorKg * peso + (10 if peso > 10 else 0)

print(f'O valor do frete é {valorTotal}')
