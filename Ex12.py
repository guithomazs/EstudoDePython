# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos
# com mais de 13 anos possuem altura inferior à média de altura desses alunos.
from random import randint
from random import uniform

dados = 2
pessoas = 30
idade = 0
altura = 1

program = [[0 for i in range(dados)]for i in range(pessoas)]
media_altura = 0
menor_media = 0

for i in range(pessoas):
    program[i][idade] = randint(10, 19)   # idades

    if program[i][idade] < 14:
        program[i][altura] = uniform(1, 1.4)  # altura

    elif program[i][idade] < 17:
        program[i][altura] = uniform(1.5, 1.9)  # altura

    else:
        program[i][altura] = uniform(1.6, 2)   # altura

    media_altura += program[i][altura]

media_altura /= pessoas

for i in range(pessoas):
    if program[i][idade] > 13:
        if program[i][altura] < media_altura:
            menor_media += 1

for i in range(pessoas):
    print(f'A idade da {i+1}ª pessoa é de {program[i][idade]} anos e tem '
          f'{program[i][altura]:.2f} metros de altura')

print(f'O número de pessoas com mais de 13 anos e menor que a média é de {menor_media}')
print('A média é de {:.2f}'.format(media_altura))