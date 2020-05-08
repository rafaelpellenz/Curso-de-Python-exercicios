maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input('Peso da {}ª pessoa: '.format(c+1)))
    if c==0:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            totmaior = peso
        if peso < menor:
            totmenor = peso
print('O maior peso lido foi de {:.1f}kg'.format(maior))
print('O menor peso lido foi de {:.1f}kg'.format(menor))