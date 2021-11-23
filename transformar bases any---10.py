parar = ['parar', 'stop', '', ' ', 'n']
a_somar = []
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
    print(a_somar)
print(sum(a_somar))