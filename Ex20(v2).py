# possível inserção do número de colaboradores.
import random

piso_abono = 100.00
num_minimos = 0
porcentagem = 0.2

qtd_minima = 15
vezes = 0
menor_automatico = 100
maior_automatico = 5000

maior = 0
abonos = []
salarios = []
s = 's'
parar = ['0', 'parar', '', ' ', 'stop', 'p']
resposta = input(f'Deseja falar o número de colaboradores?(S/N)').lower()

resposta1 = input(f'Deseja salários automáticos(serão inseridos no minimo {qtd_minima} salários '
                  f'num intervalo entre {menor_automatico} e {maior_automatico})? ').lower()

if s not in resposta:

    if s not in resposta1:   # número de colaboradores não especificado, inserção manual

        print('============================================')
        salario = input('Salário(0 = parar): ')

        while salario not in parar:
            while type(salario) != float:
                try:
                    if salario.lower() in parar:
                        break

                    salario = float(salario)
                    if salario < 0:
                        salario = input('Salário não pode ser negativo, redigite um salário válido: ')

                    elif 0 < salario < menor_automatico:
                        salario = input(f'Salário deve ser de no mínimo {menor_automatico}: ')

                    elif salario > maior_automatico:
                        salario = input(f'Salário deve ser de no máximo {maior_automatico}: ')

                except ValueError:
                    salario = input('Redigite um salário válido: ')

            if salario.lower() in parar:
                break

            salarios.append(salario)
            abono = salario * porcentagem

            abonos.append(piso_abono if abono < piso_abono else abono)
            num_minimos += int(abono < piso_abono)

            salario = input('Salário(0 = parar): ').lower()
            if salario in parar:
                break

        print('Parando de receber dados!')
        print('============================================')

    else:  # número de colaboradores não especificado, inserção automática

        continua = 1
        probabilidade = [1] + [random.randint(10, 30)for i in range(qtd_minima)]
        seletor = random.Random()

        while continua != 0:
            vezes += 1

            if vezes > qtd_minima:
                # altere a proporção entre 5(chance de parar) e 100(de continuar) para modificar a chance de continuar
                continua = seletor.choices([0, 1], [5, 100], k=1)[0]

            reais = random.randint(menor_automatico, maior_automatico)
            centavos = random.random()
            salario = round(reais + centavos, 2)

            salarios.append(salario)

            abono = salario * porcentagem

            if abono <= piso_abono:
                abonos.append(piso_abono)
                num_minimos += 1

            else:
                abonos.append(round(abono, 2))
else:

    qtd = input('Digite o número de colaboradores: ')

    while type(qtd) != int:
        try:

            qtd = int(qtd)
            if qtd <= 0:
                qtd = input('O número de colaboradores deve ser no mínimo 1, redigite um valor válido: ')

        except ValueError:
            qtd = input('Redigite um número válido: ')

    if s not in resposta1:   # número de colaboradores especificado, inserção manual

        print('Você pode parar a execução do programa a qualquer momento digitando'
              ' "Parar" ou "Stop" ou deixando em branco!')

        for i in range(qtd):

            salario = input(f'Salário {i+1}: ')

            if salario.lower() in parar:
                break

            while type(salario) != float:
                try:

                    if salario.lower() in parar:
                        break

                    salario = float(salario)
                    if salario < 0:
                        salario = input('Salário não pode ser negativo, redigite um salário válido: ')

                    elif 0 < salario < menor_automatico:
                        salario = input(f'Salário deve ser de no mínimo {menor_automatico}: ')

                    elif salario > maior_automatico:
                        salario = input(f'Salário deve ser de no máximo {maior_automatico}: ')

                except ValueError:
                    salario = input('Redigite um salário válido: ')

            if salario.lower() in parar:
                break

            salarios.append(salario)
            abono = salario * porcentagem

            abonos.append(piso_abono if abono < piso_abono else abono)
            num_minimos += int(abono < piso_abono)

        print('Parando de receber dados!')
        print('============================================')

    else:   # número de colaboradores especificado, inserção automática

        for i in range(qtd):

            reais = random.randint(menor_automatico, maior_automatico)
            centavos = random.random()
            salario = round(reais + centavos, 2)

            salarios.append(salario)
            abono = salario * porcentagem

            if abono <= piso_abono:

                abonos.append(piso_abono)
                num_minimos += 1

            else:
                abonos.append(round(abono, 2))

for i in range(len(abonos)):
    if abonos[i] > maior:
        maior = abonos[i]

print()
print('  Salário -  abono')
for i in range(len(salarios)):
    print(f'R$ {round(salarios[i], 2):>6} - R$ {round(abonos[i], 2):<5}')

print()
print(f'Foram processados {len(salarios)} colaboradores.')
print(f'Total gasto com abonos: R$ {round(sum(abonos), 2)}')
print(f'Valor mínimo pago a {num_minimos} colaboradores.')
print(f'Maior valor de abono pago: R$ {round(maior, 2)}')