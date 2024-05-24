genero = input('Qual seu gênero (M/F)? ')
idade = int(input('Qual sua idade? '))
tempoDeServico = int(input('Qual seu tempo de serviço? '))

print (((genero == 'F' and idade >= 60 ) or (genero == 'M' and idade >= 65)) or (tempoDeServico >= 30) or (idade >= 60 and tempoDeServico >= 25))
