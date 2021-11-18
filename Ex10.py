# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
# terceiro vetor de 20 elementos,cujos valores deverão ser compostos pelos
# elementos intercalados dos dois outros vetores.
from random import randint
vetorA = []
vetorB = []
vetorC = []
tamanho = 10
for i in range(tamanho):
    vetorB.append(randint(0, 20))
    vetorA.append(randint(0, 20))
print(f'Vetor 1 = {vetorA}')
print(f'Vetor 2 = {vetorB}')

for i in range(tamanho):
    vetorC.append(vetorA[i])
    vetorC.append(vetorB[i])
print(f'Vetores intercalados = {vetorC}')
print()
vetorA.sort()
vetorB.sort()
print(f'Vetor 1 ordenado = {vetorA}')
print(f'Vetor 2 ordenado = {vetorB}')
del vetorC
vetorC = []
for i in range(tamanho):
    vetorC.append(vetorA[i])
    vetorC.append(vetorB[i])
print(f'Vetores intercalados pós ordenação = {vetorC}')
vetorC.sort()
print(f'Vetor intercalado ordenado = {vetorC}')
