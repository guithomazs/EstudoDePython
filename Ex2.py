# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
from random import uniform
vetor = []
vetNums = []
qtd = 10
letra = 's'
print('Números reais!')
resposta = input('Deseja números automáticos?(S/N) ')
for i in range(qtd):
    if letra in resposta.lower():
        vetor.append(uniform(0, 20))
    else:
        vetor.append(input(f'Elemento {i+1}: '))


for i in range(qtd -1, -1, -1):
    try:
        vetor[i] = float('{:.2f}'.format(float(vetor[i])))
        vetNums.append(i)
    except:
        print(f'O elemento {i} não é um float!')

print(f'Vetor original = {vetor}')
vetor.reverse()
print(f'Invertido = {vetor}')
try:
    vetNums.sort()
    print(f'Apenas os números!')
    print(f'Crescente = {vetNums}')
    vetNums.reverse()
    print(f'Decrescente = {vetNums}')
except:
    pass