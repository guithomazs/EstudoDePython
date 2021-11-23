# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base
# em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela
# semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais
# 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores)
# que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# 1 - $200 - $299
# 2 - $300 - $399
# 3 - $400 - $499
# 4 - $500 - $599
# 5 - $600 - $699
# 6 - $700 - $799
# 7 - $800 - $899
# 8 - $900 - $999
# 9 - $1000 em diante
# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer
# vários ifs aninhados.

import random
qtdVendedores = 40
salarioFixo = 200
porcentagem = 9
comissao = porcentagem / 100
# comissao = 0.09
vendas_semana = [salarioFixo + random.uniform(0, 11000) * comissao for i in range(qtdVendedores)]
posi = [0]*9


def faixa_salarial(salario) -> int:
    inicial = int((salario - 200) // 100)
    return 9 if inicial > 8 else inicial + 1


for i in range(qtdVendedores):

    faixa = faixa_salarial(vendas_semana[i])
    posi[faixa-1] += 1
    print(f'O vendedor {i+1} recebeu R${round(float(vendas_semana[i]), 2)} '
          f'- faixa salarial:', faixa_salarial(vendas_semana[i]))

for i in range(len(posi)):
    print(f'Faixa {i+1} = {posi[i]}')