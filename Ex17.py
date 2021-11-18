# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do
# atleta será determinado pela média dos cinco valores restantes.Você deve fazer um programa que
# receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome,
# os saltos e a média dos saltos.O programa deve ser encerrado quando não for informado o nome do
# atleta.A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvelo
# Primeiro Salto: 6.5m
# Segundo Salto: 6.1m
# Terceiro Salto: 6.2m
# Quarto Salto: 5.4m
# Quinto Salto: 5.3m
# Resultado final:
# Atleta: Rodrigo Curvelo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m
vez = 0
nomes = []
Npulos = 5
medias = []
atletas = [[]]
stop = ['', ' ', 'parar', 'stop']
nome = input('Digite o Nome do atleta: ')
while nome not in stop:
    atleta = []
    nomes.append(nome)
    for i in range(Npulos):
        atleta.append(input(f'Salto {i+1}: '))
        while type(atleta[i]) != float:
            try:
                atleta[i] = float(atleta[i])
            except ValueError:
                atleta[i] = input('Digite um número válido por favor: ')
    medias.append(sum(atleta) / len(atleta))
    print('Resultado Final: ')
    print('Nome do atleta: ', nomes[vez])
    for i in range(Npulos):
        print(f'Salto {i+1} = ', atleta[i])
    print(f'Média dos saltos = {medias[vez]:.2f}')
    vez += 1
    atletas.append(atleta)
    nome = input('Digite o Nome do atleta: ')
    if nome in stop:
        print('Parando!')
        break
    del atleta

print()
print('Resultados de todos:')
print('===================================================================')
for i in range(len(nomes)):
    print('Nome:', nomes[i], end=' | ')
    for j in range(Npulos):
        print(atleta[j], end=' | ')
    print(f'Média = {medias[i]:.2f}')
    print('===================================================================')
print("End!")