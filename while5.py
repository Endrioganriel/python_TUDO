qtd_linhas = 5
qtd_colunas = 5

"""
A cada execuçao no linha, vai executar 5 do while coluna(vai executar o while interno
enquanto ele for true, ou seja, ate coluna for maior que 6)
"""
linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
 

print("Acabou")