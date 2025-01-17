"""
Metodos uteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um indice 
    clear - limpa 
    extend - estende a lista
    + - concatena a lista

"""

lista = [10, 20, 30, 40]
lista.append('bel')
nome = lista.pop()

lista.insert(0, 5)# (indice, qual valor)
# print(lista[5]) indice que nao existe
print(lista)