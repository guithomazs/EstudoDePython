# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no
# seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
from random import randint
from random import uniform
idade_max = 110
idade_min = 10
altura_max = 2.10
altura_min = 1


def validador(idade):
    while True:
        try:
            idade = int(idade)
            if idade_min <= idade <= idade_max:
                return idade
            else:
                idade = input(f'Idade deve estar entre o intervalo de {idade_min} e {idade_max}:  ')
        except ValueError:
            idade = input('Idade deve ser um número inteiro: ')


def validador2(altura):
    while True:
        try:
            altura = float(altura)
            if altura_min <= altura <= altura_max:
                return altura
            else:
                altura = input(f'Altura deve estar entre o intervalo de {altura_min} e {altura_max}: ')
        except ValueError:
            altura = input('Altura deve ser um número: ')


dados = 2
pessoas = 5
program = [[0 for i in range(dados)]for i in range(pessoas)]

resposta = input('Deseja números aleatórios? ')
if 's' in resposta:
    for i in range(pessoas):
        program[i][0] = randint(15, 60)   # números apenas ilustrativos
        program[i][1] = uniform(1.5, 2)   # números apenas ilustrativos

else:
    for i in range(pessoas):

        idade = input(f'Digite a idade da {i+1}ª pessoa: ')
        idade = validador(idade)
        program[i][0] = idade

        altura = input(f'Digite a altura da {i+1}ª pessoa: ')
        altura = validador2(altura)
        program[i][1] = altura

for i in range(pessoas - 1, -1, -1):
    print(f'A idade da {i+1}ª pessoa é de {program[i][0]} anos e tem {program[i][1]:.2f} metros de altura')