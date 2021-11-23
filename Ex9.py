# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.
from random import randint

vet = []
vetQuadrada = []

for i in range(10):
    vet.append(randint(0, 20))
    vetQuadrada.append(vet[i] ** 2)

print(f'Vetor original = {vet}')
print('Soma dos quadrados dos elementos =', sum(vetQuadrada))