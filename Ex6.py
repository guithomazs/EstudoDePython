# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
# vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
from random import randint
alunos = 10
numNotas = 4
aprovados = 0
notas = [[0 for i in range(numNotas)]for i in range(alunos)]
medias = [0 for i in range(alunos)]

for i in range(alunos):
    validador = True
    for j in range(numNotas):
        # notas[i][j] = float(input(f'Digite a n{j+1} do aluno {i+1}: '))
        # if not 0 <= notas[i][j] <= 10:
        #     while validador:
        #         print('Nota inválida! intervalo deve ser de 0 a 10')
        #         notas[i][j] = float(input(f'Digite a n{j+1} do aluno {i+1}: '))
        #         if 0 <= notas[i][j] < 10:
        #             validador = False
        notas[i][j] = randint(0, 10)

    for j in range(numNotas):
        medias[i] += notas[i][j]
    medias[i] = medias[i] / (numNotas)
    if medias[i] >= 7:
        aprovados += 1

print(f'Número de aprovados: {aprovados}. (Média maior ou igual 7)')
for i in range(alunos):
    print(f'Aluno {i+1} = {notas[i]}. Média = {medias[i]}.')