# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene
# os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
from random import randrange

vet = []
vetPar = []
vetImpar = []
qtd = 20
for i in range(qtd):
    # vet[i] = int(input(f'{i+1}- Digite um número inteiro: '))
    vet.append(randrange(10000))
    if vet[i] % 2 == 0:
        vetPar.append(vet[i])
    else:
        vetImpar.append(vet[i])
print(vet)
print(f'Vetor par = {vetPar}')
print(f'Vetor Impar = {vetImpar}')