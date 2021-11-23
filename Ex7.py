# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
from random import randint

nums = []
soma = 0
multip = 1

for i in range(5):
    nums.append(randint(0, 20))
    multip *= nums[i]

print('Soma =', sum(nums))
print(f'Multiplicação = {multip}')

for i in range(5):
    print(f'Número {i+1} = {nums[i]}')