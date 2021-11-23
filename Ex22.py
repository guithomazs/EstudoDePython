# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a
# intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar
# todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para
# verificar o que se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento.
# O programa deverá receber um número indeterminado de entradas, cada uma contendo:
# um número de identificação do mouse e o tipo de defeito:
# necessita da esfera;
# necessita de limpeza;
# a.necessita troca do cabo ou conector; quebrado ou inutilizado.
# Uma identificação igual a zero encerra o programa.
# Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100
#
# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%
import random
import string

parar = ['parar', 'stop', 'p', '', ' ', '0']

tipos_problemas = ['esfera', 'limpeza', 'troca', 'quebrado']
frases = ['necessitando da esfera', 'necessitando de limpeza',
          'necessitando troca do cabo ou conector', 'quebrado ou inutilizado']
nproblemas = len(tipos_problemas)
problemas = [0]*nproblemas
percentual = [0]*nproblemas

tamanho = [7, 8, 9, 10]
identificador = []
mouses = []

qtd_minima = 100
qtd = 0
prob = 1
resposta = input(f'Deseja valores automáticos?(serão conferidos no mínimo {qtd_minima} mouses): ').lower()

if 's' in resposta:

    while prob != 0:

        # gerando uma identificação aleatória para cada mouse
        identificador.append(''.join(random.choice(string.ascii_letters + string.digits)
                             for _ in range(random.choice(tamanho))))

        menor = 1 if qtd < qtd_minima else 0

        probabilidade = [1] + [random.randint(10, 30) for i in range(nproblemas)]   # pesos aleatórios

        prob = random.choices(range(menor, nproblemas + 1), probabilidade[menor:], k=1)[0]
        print(qtd, probabilidade, prob)

        identificador.append(prob)
        mouses.append(identificador)
        qtd += 1
        identificador = []

else:

    resposta = input('Deseja colocar apenas o número de mouses que apresentaram cada defeito? ').lower()

    if 's' in resposta:

        print('Os possíveis problemas são: ')

        for i in range(nproblemas):
            print(f'{i+1}- {frases[i]} ')

        for _ in range(nproblemas):
            prob = input(f'Quantos mouses estão {frases[_]}? ')

            while type(prob) != int:
                try:

                    prob = int(prob)
                    if prob < 0:
                        prob = input('O número não pode ser negativo: ')

                except ValueError:
                    prob = input('Digite um número inteiro corretamente: ')

            prob = 1 * prob
            problemas[_] = prob

    else:

        print()
        print(f'Um identificador aleatório de tamanho entre {tamanho[0]} e'
              f' {tamanho[-1]} será gerado para cada mouse')

        print()
        print('Os possíveis problemas são: ')
        for i in range(nproblemas):
            print(f'{i + 1}- {frases[i]} ')
        print()

        while prob not in parar:

            identificador.append(''.join(random.choice(string.ascii_letters + string.digits)
                                         for _ in range(random.choice(tamanho))))
            nome = identificador[0]

            prob = input(f'{nome} - Qual o número do defeito do mouse?(1 a '
                         f'{nproblemas} ou 0 para parar): ')

            while type(prob) != int:
                try:

                    if prob in parar:
                        break

                    prob = int(prob)
                    if not 0 < prob <= nproblemas:
                        prob = input(f'O intervalo digitado deve ser entre 1 e {nproblemas} ou 0 para parar')

                except ValueError:
                    prob = input('Digite um número inteiro corretamente: ')

            identificador.append(prob)
            mouses.append(identificador)
            identificador = []


for i in range(len(mouses)):

    print(f'{mouses[i][0]}'.ljust(12), end='')
    print(f'{mouses[i][1]}'.ljust(20))

    for j in range(len(problemas)):

        if j + 1 == mouses[i][1]:
            problemas[j] += 1

for i in range(len(problemas)):
    percentual[i] = round((problemas[i] * 100 / sum(problemas)), 2)

print()
print(problemas)

print()
print(f'Foram verificados {sum(problemas)} mouses.')
print('Situação'.ljust(40), 'quantidade'.ljust(20), 'percentual')
for i in range(len(problemas)):
    print(f'{i+1}- {frases[i]} '.ljust(45), f'{problemas[i]}'.ljust(17), f'{percentual[i]}%')