"""
insere diversos números em bases numéricas distintas, transforma-os em base 10, ao parar de inserir valores
ele soma em base 10 e transforma em outra base que peça, apenas até a hexadecimal
"""

parar = ['parar', 'stop', '', ' ', 'n']
a_somar = []
restos = []
letras = {chr(97+i): 10+i for i in range(6)}
digitado = input('Qual o número para ser transformado na base decimal? ').lower()
expo = len(digitado) - 1
nums = []

while digitado.lower() not in parar:  # de qualquer pra decimal

    for i in digitado:
        nums.append(letras[i] if i in letras else int(i))   # validação ternária

    base = int(input('Qual a base desse número?'))
    while type(base) != int:
        try:
            base = int(base)
        except ValueError:
            base = input('Redigite um valor válido para a base!')
    print(nums)
    for i in range(len(digitado)-1):
        nums[i] = nums[i] * (base ** expo)
        print(nums)
        expo -= 1

    print()
    print(sum(nums))

    a_somar.append(sum(nums))
    nums = []

    print()
    digitado = input('Novo número: ')
    expo = len(digitado) - 1
print(sum(a_somar))
somado = sum(a_somar)
base = int(input('Ele será transformado em qual base? '))

print(restos, somado)
while somado >= base:
    restos.append(somado % base)
    somado = somado // base
    print(restos, somado)
restos.append(somado)

if base > 9:
    for i in range(len(restos)):
        if restos[i] > 9:
            if restos[i] == 10:
                restos[i] = 'A'

            elif restos[i] == 11:
                restos[i] = 'B'

            elif restos[i] == 12:
                restos[i] = 'C'

            elif restos[i] == 13:
                restos[i] = 'D'

            elif restos[i] == 14:
                restos[i] = 'E'

            elif restos[i] == 15:
                restos[i] = 'F'

printer = ''
restos.reverse()

for i in range(len(restos)):
    restos[i] = str(restos[i])

for x in restos:
    printer += '' + x

print(printer)
a_somar = float(printer)
restos = []