contador = 0 

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Nao vai aparecer o 6 por causa do continue')
        continue
    
    if contador >= 10 and contador <= 27:
        print(f'Nao vai aparecer o: {contador}')
        continue

    print(f'Contador: {contador}')

    if contador == 40:
        break

print('Acabou')