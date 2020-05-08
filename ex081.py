lista = []

while True:

    lista.append(int(input('Digite um valor: ')))

    resp = str(input('Quer continuar? [S/N]'))

    if resp in 'Nn':
        break

lista.sort()
lista.reverse()
print('-\|/'*30)
print(f'Foram digitados {len(lista)} valores')
print(lista)
if lista.count(5) > 0:
    print(f'O valor 5 foi digitado {lista.count(5)} vezes.')
else:
    print('O valor 5 não foi digitado.')