alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

aprovados = [ n for n in alunos if notas[alunos.index(n)] >= 60]

print(aprovados)