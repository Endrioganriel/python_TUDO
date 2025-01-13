senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetiçoes infinitas')

"""
o while é usado quando voce nao sabe ao certo quntas repeticoes vai ter
"""