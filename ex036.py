valorCasa = float(input("Digite o valor da casa: R$ "))
salario = float(input('Digite o valor do salário: R$ '))
tempo = int(input('Digite em quantos anos pretende pagar: '))

teto = salario*0.3

if valorCasa/(tempo*12) < teto:
    print('\033[1;32mSeu empréstimo foi aprovado.\033[m')
    print('O valor da parcela mensal será de R$ {:.2f}.'.format(valorCasa/(tempo*12)))
elif valorCasa/(tempo*12) > teto:
    print('\033[1;31mSeu empréstimo foi negado.\033[m')
    print('As parcelas ultrapassam 30% da sua renda mensal.')