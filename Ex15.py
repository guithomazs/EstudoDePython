# Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

digitados = []
validador = True
continuar = True

parar = ['-1', 'parar', 'stop', '', ' ', -1]

qtd = 0
media = 0
qtdMedia = 0
abaixo_sete = 0

digitado = input('Digite uma nota no intervalo de 0 a 10(-1 ou "stop" para parar): ')
if digitado not in parar:
    while continuar:

        validador = True
        while validador:
            try:

                digitado = float(digitado)
                if type(digitado) == float:

                    if digitado in parar:
                        break

                    elif 0 <= digitado <= 10:
                        digitados.append(digitado)
                        qtd += 1

                        if digitado < 7:
                            abaixo_sete += 1

                        validador = False

                    else:
                        digitado = input("Por favor redigite essa nota: ")

                        if digitado in parar:
                            break
                else:
                    if digitado in parar:
                        break
            except:
                if digitado in parar:
                    break
            if digitado in parar:
                break
        if digitado in parar:
            break

        digitado = input('Digite uma nota no intervalo de 0 a 10(-1 ou "stop" para parar): ')

        if digitado in parar:
            continuar = False

if sum(digitados) > 0:
    media = sum(digitados) / qtd

for i in range(len(digitados)):
    if digitados[i] > media:
        qtdMedia += 1

print(digitados)
for i in range(len(digitados)):
    print(digitados[i], end='  ')
print()

digitados.reverse()
for i in range(len(digitados)):
    print(digitados[i])


print(f'Foram lidos {len(digitados)} números.')
print(f'Soma = {sum(digitados)}')
print(f'Média = {media:.2f}')
print(f'quantidade de valores acima da média calculada = {qtdMedia}')
print(f'Quantidade de valores abaixo de 7 = {abaixo_sete}')
print('Encerrando!')