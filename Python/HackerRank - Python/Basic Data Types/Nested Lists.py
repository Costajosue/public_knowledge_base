if __name__ == '__main__':
        estudantes = []

        for _ in range(int(input(f'Digite a quantidade de alunos: '))):
                nome = str(input(f'Digite o nome do aluno: '))
                nota = float(input(f'Por favor digite a nota do aluno: '))
                estudantes.append([nome, nota])
        notas = sorted(set(nota for nome, nota in estudantes)) 
        # print(sorted(nome for nome, nota in estudantes if nota == notas[1]))
        menores = sorted(nome for nome, nota in estudantes if nota == notas[1])
        for i in menores:
                print(f'{i}\n')

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39