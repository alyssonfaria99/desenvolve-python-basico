n = int(input('Quantidade de experimentos: '))

contador = 0
quantiaTotal = 0
quantiaSapo = 0
quantiaRato = 0
quantiaCoelho = 0

while contador < n:
    quantia = int(input('Quantia: '))
    tipo = input('Tipo (S, R ou C): ')
    quantiaTotal += quantia
    if tipo == 'S':
        quantiaSapo += quantia
    elif tipo == 'R':
        quantiaRato += quantia
    elif tipo == 'C':
        quantiaCoelho += quantia
    contador += 1

percentualSapos = quantiaSapo / quantiaTotal * 100
percentualCoelhos = quantiaCoelho / quantiaTotal * 100
percentualRatos = quantiaRato / quantiaTotal * 100


print(f'Total: {quantiaTotal} cobaias \nTotal de coelhos: {quantiaCoelho}\nTotal de ratos: {quantiaRato}\nTotal de sapos: {quantiaSapo}\nPercentual de coelhos: {percentualCoelhos:.2f} % \nPercentual de ratos: {percentualRatos:.2f} % \nPercentual de sapos: {percentualSapos:.2f} %')