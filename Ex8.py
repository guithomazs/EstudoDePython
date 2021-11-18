# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no
# seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
from random import randint
from random import uniform
dados = 2
pessoas = 5
program = [[0 for i in range(dados)]for i in range(pessoas)]
for i in range(pessoas):
    program[i][0] = randint(15, 60)   # números apenas ilustrativos
    program[i][1] = uniform(1.4, 2)   # números apenas ilustrativos

for i in range(pessoas - 1, -1, -1):
    print(f'A idade da {i+1}ª pessoa é de {program[i][0]} anos e tem {program[i][1]:.2f} metros de altura')