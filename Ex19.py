# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande
# quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
#
# As possíveis respostas são:
#
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao
# final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra
# a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem
# sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes
# e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
#
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800
#
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
import random

minimo = 8500
sists = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'HP/UX', 'Solaris', 'Outro']
Nsistemas = len(sists)   # atualiza todo o programa ao simplesmente inserir o nome em sists
sistemas = [0]*Nsistemas
Nvotos = 0
digitado = 1

percent = [0]*Nsistemas
maior = 0
indice = 0

print('Sistemas: ', end='')
for i, n in enumerate(sists, 1):
    print(i, '=', n, end=' | ')
print()

resposta = input(f'Deseja valores automáticos?(computará no mínimo {minimo} valores aleatórios)')
# resposta = 'sim'

if 's' not in resposta.lower():   # Inserção manual de valores
    digitado = input(f'Digite um valor de 1 a {Nsistemas} para votar no sistema operacional(0 para parar):')

    while digitado != 0:
        while type(digitado) != int:
            try:

                digitado = int(digitado)
                if digitado == 0:
                    break

            except ValueError:
                digitado = input('Digite um valor correto por favor!')
                if digitado == '0':
                    break

        if not 1 <= digitado <= Nsistemas:

            while not 1 <= digitado <= Nsistemas:
                if digitado == 0:
                    break

                digitado = input(f'Intervalo deve estar entre 1 e {Nsistemas}:')

                while type(digitado) != int:
                    try:
                        digitado = int(digitado)

                    except ValueError:
                        digitado = input('Digite um valor correto por favor!')

        if digitado == 0:
            break

        sistemas[digitado - 1] += 1
        Nvotos += 1
        digitado = input(f'Digite um valor de 1 a {Nsistemas} para votar no sistema operacional(0 para parar):')
    print('Encerrando')

else:   # Inserção automática de valores

    seletor = random.Random()
    # pesos aleatórios para cada índice
    probabilidade = [1] + [random.randint(10, 30)for i in range(Nsistemas)]

    # 3 jogos a cada 10 virão díspares, com resultados influenciados.
    if random.randint(1, 10) > 7:

        # o range do peso do candidato que virá com vantagem
        probabilidade[random.randint(1, Nsistemas-1)] = random.randint(30, 50)

    while digitado != 0:
        menor_opcao = 1 if Nvotos < minimo else 0
        digitado = seletor.choices(range(menor_opcao, Nsistemas+1), probabilidade[menor_opcao:], k=1)[0]

        if digitado == 0:
            break

        sistemas[digitado - 1] += 1
        Nvotos += 1


if Nvotos > 0:
    for i in range(len(sistemas)):
        percent[i] = sistemas[i] * 100 / Nvotos

        for j in range(len(sistemas)):
            if sistemas[j] > sistemas[i] and sistemas[j] > maior:
                maior = sistemas[j]
                indice = j

print()
print('Foram computados', Nvotos, 'votos!')
print('------------------------------------------------------')
print('Sistema Operacional             votos             %')
print('------------------------------------------------------')
for i in range(len(sistemas)):
    print(f'{sists[i]:<20}', end='  ')
    print(f'{sistemas[i]:^25}', end=' ')
    print(f'{percent[i]:.2f}%')
print('------------------------------------------------------')
print(f'O sistema mais votado foi o {sists[indice]} com {sistemas[indice]} votos,'
      f' correspondendo a aproximadamente {round(percent[indice])}% dos votos! ')