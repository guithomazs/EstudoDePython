# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
qtd_notas = 4
vetorA = [0]*qtd_notas
soma = 0


def is_digit(x):
    while type(x) != float:
        try:
            x = float(x)
            return x
        except ValueError:
            x = input('Você precisa digitar um número: ')


for i in range(qtd_notas):
    x = input(f'Digite a n{i+1}: ')

    x = is_digit(x)

    vetorA[i] = float(x)
    soma += vetorA[i]

media = soma / qtd_notas
print(f'Média = {media}')

for i in range(qtd_notas):
    print(vetorA[i])