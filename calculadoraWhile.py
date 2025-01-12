""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    opr = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_int1 = float(numero_1)
        num_int2= float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if opr not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(opr) > 1:
        print('Digite apenas um operador.')
        continue

    ###
    if opr == '+':
        resultado = num_int1 + num_int2
        print(f'A soma de {num_int1} + {num_int2} é: {resultado}')

    elif opr == '-':
        resultado = num_int1 - num_int2
        print(f'A subtração de {num_int1} - {num_int2} é: {resultado}')

    elif opr == '*':
        resultado = num_int1 * num_int2
        print(f'A multiplicação de {num_int1} * {num_int2} é: {resultado}')

    elif opr == '/':
        resultado = num_int1 / num_int2
        print(f'A divisão de {num_int1} / {num_int2} é: {resultado}')

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break