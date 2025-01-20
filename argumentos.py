"""
Argumentos nomeados tem nome com sinal de igual
Argumentos nao nomeados recebe apenas o argumento
"""

def soma(x, y):
    print(f'x={x} y={y}', '|', 'x + y =', x+y)
    
soma(1,2)
soma(x=1,y=2)