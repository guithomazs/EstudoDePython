# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os
# resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de
# contadores(1-6) e uma função para gerar números aleatórios, simulando os lançamentos dos dados.
import random
lados = 20
dado = [0]*lados
vezes = 100
for i in range(vezes):
    lancado = random.randrange(lados)
    dado[lancado] += 1
for i in range(len(dado)):
    print(f'O lado {i+1} do dado saiu um total de: {dado[i]} vezes')