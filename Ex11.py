# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
from random import randint
vetorA = []
vetorB = []
vetorC = []
vetorD = []
tamanho = 10

for i in range(tamanho):
    vetorA.append(randint(0, 20))
    vetorB.append(randint(0, 20))
    vetorC.append(randint(0, 20))
print(f'Vetor 1 = {vetorA}')
print(f'Vetor 2 = {vetorB}')
print(f'Vetor 3 = {vetorC}')

for i in range(tamanho):
    vetorD.append(vetorA[i])
    vetorD.append(vetorB[i])
    vetorD.append(vetorC[i])
print(f'Vetores intercalados = {vetorD}')
print()
vetorA.sort(); vetorB.sort(); vetorC.sort()
print(f'Vetor 1 ordenado = {vetorA}')
print(f'Vetor 2 ordenado = {vetorB}')
print(f'Vetor 3 ordenado = {vetorC}')
del vetorD
vetorD = []
for i in range(tamanho):
    vetorD.append(vetorA[i])
    vetorD.append(vetorB[i])
    vetorD.append(vetorC[i])
print(f'Vetores intercalados pós ordenação = {vetorD}')
vetorD.sort()
print(f'Vetor intercalado ordenado = {vetorD}')