# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
from random import uniform
vetor = []
vetNums = []
qtd = 10

print('Números reais!')
resposta = input('Deseja números automáticos?(S/N) ')

for i in range(qtd):

    if 's' in resposta.lower():
        vetor.append(uniform(0, 20))

    else:
        vetor.append(input(f'Elemento {i+1}: '))


for i in range(qtd - 1, -1, -1):

    try:
        vetor[i] = '{:.2f}'.format(float(vetor[i]))
        # vetor[i] = round(float(vetor[i]), 2)
        vetNums.append(vetor[i])

    except ValueError:
        print(f'O elemento {i} não é um float!')

print(f'Vetor original = {vetor}')
print(f'Invertido = {vetor[::-1]}')

try:
    vetNums.sort()
    print(f'Apenas os números!')
    print(f'Crescente = {vetNums}')
    print(f'Decrescente = {vetNums[::-1]}')
except:
    pass