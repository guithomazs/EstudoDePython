# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
# consoantes foram lidas. Imprima as consoantes.
from random import choice
from string import ascii_letters

vet = []
geral = []
qtd = 10

for i in range(qtd):
    letra = ''.join(choice(ascii_letters))
    # letra = input(f'{i+1} - Digite um caractere: ')

    if not ((letra.lower() == 'a') or (letra.lower() == 'e') or
            (letra.lower() == 'i') or (letra.lower() == 'o') or
            (letra.lower() == 'u')):
        vet.append(letra)
    geral.append(letra)

print(f'Apenas consoantes = {vet}', end=' ')
print()
print(f'Geral = {geral}', end=' ')