# f = open('estomago.txt')
# linhas = f.readlines()
# print('Número de linhas:', linhas)

# contador = 0
# numeroDeLinhas = 0

# for linha in f:
#     contador += 1
#     if contador <= 26:
#         print(linha)
#     else:
#         break
count = 0
maior = 0
nonato = 0
iria = 0
print("PRIMEIRAS 25 LINHAS: \n")
with open("estomago.txt","r",encoding='utf-8') as estomago:
    for linhas in estomago:
        if count < 25:
            print(linhas, end="")
        count += 1
        if len(linhas) > maior:
            maior = len(linhas)
            linha_maior =  linhas
        if "nonato" in linhas.lower():
            nonato += 1
        if "íria" in linhas.lower():
            iria += 1

    print("NÚMERO DE LINHAS DO ARQUIVO: ",count)


