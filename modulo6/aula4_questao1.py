listaPares = [n for n in range (20,51) if n % 2 == 0]
print(listaPares)

listaQuadrado = [ n ** 2 for n in range(1,10)]
print(listaQuadrado)

listaDivididoPor7 = [n for n in range (1, 101) if n % 7 == 0]
print(listaDivididoPor7)

listaParOuImpar = [ 'par' if n % 2 == 0 else 'ímpar' for n in range(0,30,3)]
print(listaParOuImpar)