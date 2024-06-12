# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

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
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

# Language
# Python 3
# More
# 1234
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
# Line: 4 Col: 31

# Test against custom input

estudantes = []# Criando uma lista para armazenas as infomações dos estudantes 

for _ in range(int(input(f'Digite a quantidade de alunos(max: 5 alunos): '))): # Criando um loop com o for (Para cada item X repetir x vezes
        nome = str(input(f'Digite o nome do aluno: '))
        nota = float(input(f'Por favor digite a nota do aluno: '))
        estudantes.append([nome, nota]) # Armezenar na lista estudantes as informações dos alunos e notas dos estudantes
# print(sorted(estudantes))
notas = sorted(set(nota for nome, nota in estudantes)) # criando uma nova lista com o sorted organizando em ordem alfabetica, utilizando o set para eliminar possiveis notas duplicadas 
print(sorted(nome for nome, nota in estudantes if nota == notas[1])) # imprimir o nome para cada nome e nota em estudante imprima a nota na possição 2 da lista notas
