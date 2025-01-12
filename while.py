# while -> enquanto...

condicao = True

while condicao:
    nome = input('qual o seu nome: ')
    print(f'Seu nome é {nome}') 

    if nome == 'sair':
        break

print('Acabou')