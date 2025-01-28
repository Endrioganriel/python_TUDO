# def duplicar_num(num):
#     def duplicar():
#         return f'O numero duplicado: {num * 2}'  
#     return duplicar
    
# def triplicar_num(num):
#     def triplicar():
#         return f'O numero duplicado: {num * 3}'  
#     return triplicar

# def quadr_num(num):
#     def quadr():
#         return f'O numero duplicado: {num * 2}'  
#     return quadr

# s1 = duplicar_num(3)
# s2 = triplicar_num(3)
# s3 = quadr_num(3)

# print(s1())
# print(s2())
# print(s3())

# Melhor assim:


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador 
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))


