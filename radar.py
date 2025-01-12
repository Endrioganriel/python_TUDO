"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

-> O isdigit()método retorna True se todos os caracteres forem dígitos, caso contrário, False.
Expoentes, como ², também são considerados um dígito.




entrada = input('Digite um numero int: ')

if entrada.isdigit():
    num = int(entrada)
    if num % 2 == 0:
        print(f'O {num} é par')
    else:
        print(f'O {num} é impar')
else:
    print('Voce nao digitou um numero inteiro')
"""
"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Que horas sao?')
try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('BOM DIAAAAAAAA')
    elif hora >=12 and hora <= 17:
        print('BOA TARDE')
    elif hora >=18 and hora <= 23:
        print('BOA NOITEEE')
    else:
        print('Nao conheco essa hora')

except:
    print('Digite um valor permitido')
"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
""" 