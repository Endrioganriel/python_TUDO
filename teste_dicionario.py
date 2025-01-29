perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    
    {
        'Pergunta': 'Quanto é 5*5',
        'Opcoes': ['1', '3', '25', '5'],
        'Resposta': '25',
    },
    
    {
        'Pergunta': 'Quanto é 10/2',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '5',
    },

]
qta_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    
    opcoes = pergunta['Opcoes']
    for i, opc in enumerate(opcoes):
        print(f'{i})', opc)
    print()
    
    escolha = input('Escolha uma opcao: ')
    
    acertou = False
    escolha_int = None
    qta_opc = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)
        
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qta_opc:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
                
    print()
    if acertou:
        qta_acertos += 1
        print('Acertou')
    else:
        print('Errou')
        
    print()
    
print('Voce acertou', qta_acertos, 'de', len(perguntas), 'perguntas.')