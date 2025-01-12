
while True:
    
    print('-----Calculadora-----')
    num1 = input('Numero 1: ')
    num_int1 = int(num1)
    num2 = input('Numero 2: ')
    num_int2 = int(num2)
    print('\n')
    print('Qual a operação?')
    print('[+] soma')
    print('[*] multipliação')
    print('[-] subtração')
    print('[/] divisão')
    
    opr = input('Digite aqui a operaçao: ')
    if opr != '*' '+' '-' '/':
        print('invalido') 
    print('\n')
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


    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break