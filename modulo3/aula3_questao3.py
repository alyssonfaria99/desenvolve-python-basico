jogadorFrequente = input('Já jogou pelo menos 3 jogos de tabuleiro?')
idade = int (input('Qual sua idade? '))
quantasVitorias = int(input('Quantas vitórias você tem? '))

print('Apto para ingressar no clube de jogos de tabuleiro:', ((idade > 15 and idade < 19) and (jogadorFrequente == 'True') and (quantasVitorias >= 1)))