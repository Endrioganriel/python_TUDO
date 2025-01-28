"""
Closure e funçoes que retornam outras funçoes
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar

s1 = criar_saudacao('Bom dia', 'Bel')
s2 = criar_saudacao('Boa noite', 'Bel')

print(s1())
print(s2())