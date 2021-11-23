# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos:
# FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos
# quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
# °O modelo do carro mais econômico;
# °Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância
# de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
# Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível
# ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
# Comparativo de Consumo de Combustível
#
# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5
#
# Relatório Final
#  1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
#  2 - gol             -   10.0 -  100.0 litros - R$ 225.00
#  3 - uno             -   12.5 -   80.0 litros - R$ 180.00
#  4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
#  5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.
import random

veiculos_feitos = ['Fusca', 'Gol', 'Uno', 'Vectra', 'Peugeout', 'Fox', 'Palio', 'Siena', 'Celta', 'Onix',
                   'Sandero', 'Fiesta', 'HB20', 'Voyage', 'Cobalt', 'Ford Ka', 'Corolla', 'Civic',
                   'Logan', 'City', 'Focus', 'Versa', 'Etios', 'Fluence', 'Jetta']
num_feitos = len(veiculos_feitos)
veiculos = []
nome = 0
km_litros = 1
indice = 0   # definido apenas para não quebrar na linha 135
litros_necessarios = []

nome_veiculos = []
empate = []
gastos = []

menor_kms_possivel = 4
maior_kms_possivel = 15
preco_gasolina = 2.25
distancia = 1000
vez = 1
parar = ['parar', 'para', 'stop', '', ' ', '  ', 'sair']
stop = 'inativo'

veiculo = input('Deseja valores aleatórios demonstrativos? ').lower()
if 's' not in veiculo:
    print('Para parar de inserir valores, escreva "parar" ou "stop" na hora de escrever o veículo!')

    while veiculo not in parar:
        veiculo = input(f'Digite o {vez}º veículo: ')
        veiculos.append(veiculo)

        if veiculo in parar:
            break

        kms = input('Km por litro: ')

        while type(kms) != float:
            try:
                kms = float(kms)
                if kms < menor_kms_possivel:
                    kms = input(f'O minimo de kms por litro possível é de {menor_kms_possivel}!: ')

                elif kms > maior_kms_possivel:
                    kms = input(f'O máximo de kms por litro possível é de {maior_kms_possivel}!: ')

            except ValueError:
                if kms in parar:
                    stop = kms
                    kms = input('Termine mais esse modelo para encerrar!: ')

                else:
                    kms = input('Por favor digite um número válido:')

        veiculos.append(kms)
        nome_veiculos.append(veiculos)
        vez += 1
        gastos.append(round((distancia / kms * preco_gasolina), 2))
        litros_necessarios.append(round(distancia / kms, 1))

        veiculos = []
        if stop in parar:
            break

else:
    qtd = input(f'Para quantos carros?(máximo de {num_feitos}):')
    print()
    while type(qtd) != int:
        try:
            qtd = int(qtd)
            if qtd < 1 or qtd > num_feitos:
                qtd = input(f'Por favor digite no intervalo entre 1 e {num_feitos}: ')

        except ValueError:
            qtd = input(f'Digite um número inteiro maior ou igual a um e menor que {num_feitos}: ')

    for i in range(qtd):

        veiculos.append(random.choice(veiculos_feitos))
        veiculos_feitos.remove(veiculos[0])

        kms = round((random.uniform(menor_kms_possivel, maior_kms_possivel)), 1)
        veiculos.append(kms)

        litros_necessarios.append(round(distancia / kms, 1))
        gastos.append(round((distancia / kms * preco_gasolina), 2))

        nome_veiculos.append(veiculos)
        print(veiculos)
        veiculos = []

menor = litros_necessarios[0]
for i in range(len(litros_necessarios)):

    if litros_necessarios[i] < menor:
        menor = litros_necessarios[i]
        indice = i
empate.append(indice)

for i in range(len(litros_necessarios)):

    if i != empate[0]:
        if menor == litros_necessarios[i]:
            empate.append(i)

print()
print('Relatório final:')
for i in range(len(nome_veiculos)):
    print(f' {i+1} - {nome_veiculos[i][nome]}'.ljust(14),
          f'-  {nome_veiculos[i][km_litros]} '.ljust(8),
          f'-  {litros_necessarios[i]} litros'.ljust(15),
          f'-  R$ {gastos[i]}'.ljust(12))

if len(empate) < 2:
    print(f'O menor consumo é o do {nome_veiculos[indice][nome]}')

else:
    print(f'O menor consumo está empatado entre:')
    for i in range(len(empate)):
        print(nome_veiculos[(empate[i])][nome])

# print()
# print(nome_veiculos)
# print(litros_necessarios)
# print(gastos)