# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
from random import randrange

vetor = []
qtd = 5
print('Números Inteiros!')

for i in range(qtd):
    vetor.append(randrange(-1000, 1000))

for i in range(len(vetor)):
    print(vetor[i])