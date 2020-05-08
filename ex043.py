print('*'*26)
print('**  \033[1mCalculadora de IMC\033[m  **')
print('*'*26)

peso = float(input('Qual é o peso do paciente em kg: '))
altura = float(input('Qual é a altura do paciente em m: '))

IMC = peso/altura**2

print('O IMC do paciente é de {:.2f}.'.format(IMC))

if IMC<18.5:
    print('\033[1;35mAbaixo do Peso\033[m')
    print('Peso Ideal')
    print('Sobrepeso')
    print('Obesidade')
    print('Obesidade Mórbida')
elif 18.5<=IMC<25:
    print('Abaixo do Peso')
    print('\033[1;35mPeso Ideal\033[m')
    print('Sobrepeso')
    print('Obesidade')
    print('Obesidade Mórbida')
elif 25<=IMC<30:
    print('Abaixo do Peso')
    print('Peso Ideal')
    print('\033[1;35mSobrepeso\033[m')
    print('Obesidade')
    print('Obesidade Mórbida')
elif 30<=IMC<40:
    print('Abaixo do Peso')
    print('Peso Ideal')
    print('Sobrepeso')
    print('\033[1;35mObesidade\033[m')
    print('Obesidade Mórbida')
elif 40<=IMC:
    print('Abaixo do Peso')
    print('Peso Ideal')
    print('Sobrepeso')
    print('Obesidade')
    print('\033[1;35mObesidade Mórbida\033[m')