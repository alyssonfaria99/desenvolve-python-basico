dataNascimento = input('Digite sua data de nascimento: ')

mes = int(dataNascimento[3:5])
meses = ['Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
mesExtenso = meses[mes - 1]

dia = int(dataNascimento[:2])
ano = int(dataNascimento[6:len(dataNascimento)])

print(f'Você nasceu em {dia} de {mesExtenso} de {ano}')