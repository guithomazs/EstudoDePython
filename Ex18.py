# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber
# qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa,
# que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para
# desenvolver este programa. Para computar cada voto, a
# telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador.
# Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for
# digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir
# outro número. Após o final da votação, o programa deverá exibir:
# O total de votos computados;
# Os números e respectivos votos de todos os jogadores que receberam votos;
# O percentual de votos de cada um destes jogadores;
# O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos
# e o percentual de votos dados a ele.
# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado
# aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá
# executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois
# parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e
# retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser
# o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
# Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto
# no disco, obedecendo a mesma disposição apresentada na tela.
# Exemplo:
# Enquete: Quem foi o melhor jogador?
#
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50
# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0
#
# Resultado da votação:
#
# Foram computados 8 votos.
#
# Jogador Votos           %
# 9               4               50,0%
# 10              3               37,5%
# 11              1               12,5%
# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
import random

parar = ['0', 'parar', ' ', '', 'stop']
Numjogadores = 23
votos = [0]*Numjogadores

voto = 0
jogador = 1
percent = 2

minimo_votos = 200
numjog = 1
qtd = 0

probabilidade = [1] + [random.randint(5, 15) for i in range(Numjogadores)]
num1 = random.randint(1, Numjogadores)   # apenas para ver qual número foi o sorteado
num2 = random.randint(1, Numjogadores)

#  deixar os números menos igualados, possuindo jogadores com destaque maior
probabilidade[num1] = random.randint(30, 50)     # o jogador de destaque
probabilidade[num2] = random.randint(20, 40)     # o segundo jogador de destaque
print(probabilidade)
print(num1)
print(num2)

jogadores = [[0 for i in range(3)]for i in range(Numjogadores)]

for i in range(Numjogadores):
    jogadores[i][1] = i

print('Enquete: Quem foi o melhor jogador?')

resposta = input('números aleatórios? ')

if 's' not in resposta.lower():
    numjog = input('Número do jogador (0 = fim): ')

    while numjog not in parar:
        while type(numjog) != int:
            try:
                numjog = int(numjog)

            except ValueError:
                numjog = input('Digite um número válido por favor: ')

        if numjog == 0:
            break

        elif 1 <= numjog <= 23:
            jogadores[numjog - 1][voto] += 1
            votos[numjog - 1] += 1

        else:
            print('Informe um valor entre 1 e 23 ou 0 para sair!')

        numjog = input('Número do jogador (0 = fim): ')
        if numjog == 0:
            break


else:
    while numjog != 0:

        menor = 1 if qtd < minimo_votos else 0

        numjog = random.choices(range(menor, Numjogadores + 1), probabilidade[menor:], k=1)[0]

        votos[numjog - 1] += 1
        jogadores[numjog - 1][voto] += 1

        qtd += 1


if sum(votos) > 0:
    for i in range(len(jogadores)):
        jogadores[i][percent] = votos[i] * 100 / sum(votos)

exibir = jogadores
jogadores.sort(reverse=True)


for i in range(Numjogadores):
    print(f'Jogador {exibir[i][jogador] + 1}'.ljust(10), f'- {exibir[i][voto]} votos')


print('--------------------------------------------------------------------')
print(f'Foram computados {sum(votos)} votos.')
print('Jogador               Votos               %')
for i in range(3):
    print(f'   {jogadores[i][jogador] + 1}'.ljust(23),
          f'{jogadores[i][voto]}'.ljust(15),
          f'{round(jogadores[i][percent], 1)}%'.ljust(2))
print('--------------------------------------------------------------------')
