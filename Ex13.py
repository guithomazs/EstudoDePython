# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
import random
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril',  'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro',  'Novembro',  'Dezembro']
temps = []
parar = ['stop', 'parar', 'para', '', ' ']
sim = 's'

resposta = input('Deseja temperaturas aleatórias? ').lower()

if sim in resposta:

    for i in range(12):
        temps.append(round(random.uniform(-10, 42), 2))

else:
    print('Você pode parar a execução do programa a qualquer momento digitando "parar"')

    for i in range(12):
        temperatura = input(f'Digite a temperatura do mês de {meses[i]} em celsius:', )

        if temperatura in parar:
            break

        while type(temperatura) != float:
            try:
                temperatura = float(temperatura)

            except ValueError:
                temperatura = input(f'Digite uma temperatura de maneira válida!')

        temps.append(temperatura)

if len(temps) > 0:
    media = round(sum(temps)/len(temps), 2)
    print()

    for i in range(12):
        print(f'{i+1} - {meses[i]}: {temps[i]}Cº')

    print()
    print('Média anual das temperaturas = ', media)
    print()
    print('Temperaturas maiores ou iguais da média:')

    for i in range(12):
        if temps[i] > media:
            print(f'Temperatura {temps[i]} Cº do mês de {meses[i]}.'.ljust(50),
                  str(i+1).rjust(2, '0'), '-', meses[i], '-', temps[i], 'Cº')

else:
    print('Nada inserido!')
print()
print('Encerrando!')