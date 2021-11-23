# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
# vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
from random import uniform

alunos = 10
numNotas = 4
aprovados = 0
notas = [[0 for i in range(numNotas)]for i in range(alunos)]
medias = [0 for i in range(alunos)]

resposta = input('Deseja notas aleatórias? ')

for i in range(alunos):
    validador = True

    for j in range(numNotas):
        if 's' not in resposta:
            notas[i][j] = float(input(f'Digite a n{j+1} do aluno {i+1}: '))

            if not 0 <= notas[i][j] <= 10:

                while validador:
                    print('Nota inválida! intervalo deve ser de 0 a 10')
                    notas[i][j] = float(input(f'Digite a n{j+1} do aluno {i+1}: '))
                    if 0 <= notas[i][j] < 10:
                        validador = False
        else:
            notas[i][j] = round(uniform(0, 10), 2)

    for j in range(numNotas):
        medias[i] += notas[i][j]

    medias[i] = round(medias[i] / numNotas, 2)
    if medias[i] >= 7:
        aprovados += 1

print(f'Número de aprovados: {aprovados}. (Média maior ou igual 7)')
for i in range(alunos):
    print(f'Aluno {i+1} = {notas[i]}. Média = {medias[i]}.')