op = 0
while not op == 1:
    sexo = str(input('Digite o sexo (M/F): '))
    if sexo in 'MmfF':
        op+=1
    else:
        print('Você digitou uma opção invalida.')
print('O sexo escolhido foi {}.'.format(sexo.upper()))