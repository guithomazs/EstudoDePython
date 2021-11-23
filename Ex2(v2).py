# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
from random import uniform
vetor = []
Nums = 0
qtd = 10

print('Números reais!')
resposta = input('Deseja números automáticos?(S/N) ')

for i in range(qtd):
    if 's' in resposta.lower():
        vetor.append(round(uniform(0, 20), 2))

    else:
        nums = input(f'{i} - Digite um número: ')
        while type(nums) != float:
            try:
                nums = float(nums)

            except ValueError:
                nums = input('Digite um número válido: ')

        vetor.append(nums)

print(f'Vetor original = {vetor}')
print(f'Invertido = {vetor[::-1]}')
vetor.sort()
print(f'Crescente = {vetor}')
print(f'Decrescente = {vetor[::-1]}')