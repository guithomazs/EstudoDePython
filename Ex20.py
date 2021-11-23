# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao
# bom resultado alcançado durante o ano que passou.Para isto contratou você para desenvolver a
# aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono. Após
# reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato
# laboral, chegou - se a seguinte forma de cálculo: a.Cada funcionário receberá o equivalente a 20 %
# do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários
# cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma
# preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades.
# Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários.
# Um valor de salário igual a 0 (zero) encerra a digitação.Após a entrada de todos os dados o programa
# deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima.
# Ao final, o programa deverá apresentar:
# O salário de cada funcionário, juntamente com o valor do abono;
# O número total de funcionário processados; O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais; O maior valor pago como abono;
# A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos.Os valores podem
# mudar a cada execução do programa. Projeção de Gastos com Abono
#
# == == == == == == == == == == == == == ==
# Salário: 1000
# Salário: 300
# Salário: 500
# Salário: 100
# Salário: 4500
# Salário: 0
#
# Salário - Abono
# R$ 1000.00 - R$  200.00
# R$  300.00 - R$  100.00
# R$  500.00 - R$  100.00
# R$  100.00 - R$  100.00
# R$ 4500.00 - R$  900.00
#
# Foram processados 5 colaboradores.
# Total gasto com abonos: R$ 1400.00
# Valor mínimo pago a 3 colaboradores
# Maior valor de abono pago: R$ 900.00
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

resposta = input(f'Deseja salários automáticos(serão inseridos no minimo {qtd_minima} salários '
                 f'num intervalo entre {menor_automatico} e {maior_automatico})? ').lower()
if s not in resposta:  # inserção manual
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
    probabilidade = [1] + [random.randint(10, 30) for i in range(qtd_minima)]
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