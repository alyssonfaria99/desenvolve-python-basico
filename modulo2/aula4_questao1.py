comprimento = int(input('Comprimento: '))
largura = int(input('Largura: '))
precoMetro2 = float(input('Preço do metro quadrado: '))

area = comprimento * largura
precoTotal = precoMetro2 * area
print('O terreno possui', area,'m² e custa R$',precoTotal)