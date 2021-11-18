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
def m7(v):
    for i in v:
        if i < 7:
            yield i


def m7v2(v):
    k = 0
    for i in v:
        if i < 7:
            k += 1
    return k


def m7v3(v):
    k = 0
    for i in v:
        k += int(i < 7)
    return k


parar = ['-1', 'parar', 'stop', '', ' ']
vetor = []
while True:
    n = input('Digite um número(-1 para parar): ')
    if n.strip() in parar:
        break
    if n == '' or not n.isdecimal():
        print('Valor incorreto, preencha novamente!')
        continue
    if 0 <= float(n) <= 10:
        vetor.append(float(n))
    else:
        print('Fora do intervalo de 0 a 10!')

print('Quantidade de itens lidos: ', len(vetor))
print('Elementos em ordem: ', vetor)
print('Ordem inversa: ')
print('', '\n '.join([str(i) for i in vetor[::-1]]))
print('Soma = ', sum(vetor))
media = sum(vetor)/len(vetor)
print('Média = ', media)
menor_sete = 0
for i in range(len(vetor)):
    if vetor[i] < 7:
        menor_sete += 1
print('Maior que a média = ', sum([1 for i in vetor if i > media]))    # atenção depois
print('Menor que sete = ', menor_sete)
print('Menor que sete2 = ', len(list(filter(lambda x: x < 7, vetor))))
print('Menor que sete3 = ', len([1 for i in vetor if i < 7]))        # atenção depois
print('Menor que sete4 = ', len(list(m7(vetor))))
print('Menor que sete5 = ', m7v2(vetor))
print('Menor que sete6 = ', m7v3(vetor))
print('Fim')