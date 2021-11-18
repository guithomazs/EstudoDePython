# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
vetorA = [0]*4
soma = 0
for i in range(4):
    num = input(f'Digite a n{i+1}: ')
    if not num.isdigit():
        print('você precisa digitar um número!')
        continue
    vetorA[i] = float(num)
    soma += vetorA[i]
media = soma / 4
print(f'Média = {media}')
for i in range(4):
    print(vetorA[i])