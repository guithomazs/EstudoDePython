digitado = input('Qual o número(em base decimal) a ser transformado? ').lower()
restos = []
parar = ['parar', 'stop', '', ' ', 'n']

while digitado.lower() not in parar:
    base = input('Ele será transformado em qual base? ')
    while type(base) != int:
        try:
            base = int(base)
        except ValueError:
            base = input('Redigite um valor válido para a base!')
            if base in parar:
                break
    if base in parar:
        break
    dividido = int(digitado)

    print(restos, dividido)
    while dividido >= base:
        restos.append(dividido % base)
        dividido = dividido // base
        print(restos, dividido)
    restos.append(dividido)

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

    digitado = input('Qual o número(em base decimal) a ser transformado? ').lower()