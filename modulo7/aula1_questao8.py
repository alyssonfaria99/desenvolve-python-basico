def pedirCpf():
    global cpf 
    cpf = input('Digite seu cpf (XXX.XXX.XXX-XX): ')
    return cpf

def calcularPrimeiroVerificador():
    arrStr = [n for n in cpf if n in '0123456789']
    arrNumeros = [int(n) for n in arrStr]
    soma = 0
    multiplicador = 10
    for numero in arrNumeros[:9]:
        soma += numero * multiplicador
        multiplicador -= 1
    primeiroVerificador = 0 if soma % 11 < 2 else 11 - (soma % 11)
    return primeiroVerificador


def calcularSegundoVerificador():
    primeiroVerificador = calcularPrimeiroVerificador()
    arrStr = [n for n in cpf if n in '0123456789']
    arrNumeros = [int(n) for n in arrStr]
    arrNumeros = arrNumeros[:9]
    arrNumeros.append(primeiroVerificador)
    soma = 0
    multiplicador = 11
    for numero in arrNumeros[:10]:
        soma += numero * multiplicador
        multiplicador -= 1
    segundoVerificador = 0 if soma % 11 < 2 else 11 - (soma % 11)
    return segundoVerificador

def verificarCpf():
    primeiroVerificador = calcularPrimeiroVerificador()
    segundoVerificador = calcularSegundoVerificador()
    print(primeiroVerificador, segundoVerificador)
    if (int(cpf[12]) == primeiroVerificador and int(cpf[13]) == segundoVerificador):
        print('Válido')
    else:
        print('Inválido')

pedirCpf(), verificarCpf()




