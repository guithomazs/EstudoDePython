
letras2 = [str(i) if i < 10 else chr(87+i) for i in range(16)]
digitado = input('Qual o número(em base decimal) a ser transformado? ').lower()
restos = []
parar = ['parar', 'stop', '', ' ', 'n']

while digitado.lower() not in parar:
    base = int(input('Ele será transformado em qual base? '))
    dividido = int(digitado)
    while dividido >= base:
        restos.append(letras2[dividido % base])
        dividido = dividido // base
    restos.append(letras2[dividido])
    printer = ''.join(restos[::-1])
    print(printer)
    restos = []
    digitado = input('Qual o número(em base decimal) a ser transformado? ').lower()