# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a - "Telefonou para a vítima?"
# b - "Esteve no local do crime?"
# c - "Mora perto da vítima?"
# d - "Devia para a vítima?"
# e - "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
frases = ['Telefonou para a vítima? ', 'Esteve no local do crime? ', 'Mora perto da vítima? ',
          'Devia para a vítima? ', 'Já trabalhou com a vítima? ']
respostas = []
sim = 's'

Rpositivas = 0
veredito = 'inocente'

for i in range(len(frases)):
    respostas.append(input(frases[i]))

if 'j' in respostas[-1].lower():
    respostas[-1] = 's'

for i in range(len(respostas)):
    if sim in respostas[i].lower():
        Rpositivas += 1

if Rpositivas == 2:
    veredito = 'Suspeita'

elif 3 <= Rpositivas <= 4:
    veredito = 'Cúmplice'

elif Rpositivas == 5:
    veredito = 'Assassino'

print('Veredito = {:s}'.format(veredito))