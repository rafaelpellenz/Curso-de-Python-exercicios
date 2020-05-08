lista = list()

while True:

    val = int(input('Digite um valor: '))

    if val not in lista:
        lista.append(val)

    else:
        print('Valor duplicado! Não vou adicionar...')

    resp = str(input('Quer continuar? [S/N]'))

    if resp in 'Nn':
        break

lista.sort()
print(f'Você digitou os valores {lista}')
