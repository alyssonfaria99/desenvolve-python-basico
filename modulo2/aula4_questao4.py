entrada = 576

notasDe100 = 576 // 100
restoDe100 = 576 % 100

notasDe50 = restoDe100 // 50
restoDe50 = restoDe100 % 50

notasDe20 = restoDe50 // 20
restoDe20 = restoDe50 % 20

notasDe10 = restoDe20 // 10
restoDe10 = restoDe20 % 10

notasDe5 = restoDe10 // 5
restoDe5 = restoDe10 % 5

notasDe2 = restoDe5 // 2
restoDe2 = restoDe5 % 2

notasDe1 = restoDe2 // 1

print(f'{notasDe100} nota(s) de 100 \n{notasDe50} nota(s) de 50 \n{notasDe20} nota(s) de 20 \n{notasDe10} nota(s) de 10 \n{notasDe5} nota(s) de 5 \n{notasDe2} nota(s) de 2 \n{notasDe1} nota(s) de 1')