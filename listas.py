"""
Listas de listas e seus indices
"""

salas = [
    #  0         1
    ['Maria', 'Helena'],#0
    #   0 
    ['lena'],#1
    #   0        1        2 
    ['Jose', 'Eduardo', 'Marcos'],#2 
    
    
]
#print(salas[1][0])
#print(salas[2][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)