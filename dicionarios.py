pessoa = {
    'nome' : 'Endrio gabriel',
    'sobrenome' : 'Souza',
    'idade' : 23,
    'altura' : 1.8,
    'enderecos' :[
        {'rua': 'TATATATa', 'numero': 123},
        {'rua': 'outro TATATATa', 'numero': 123},
    ],
}

# criando uma nova chave

pessoa['cidade'] = 'Manaus'

print(pessoa) 
print('\n\n\n')

pessoa['nome'] = 'jaburu'
del pessoa['idade']

print(pessoa['nome']) 
print('\n\n\n')
print(pessoa) 


