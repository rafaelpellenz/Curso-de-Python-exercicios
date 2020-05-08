salario = float(input('Digite o salário do funcionário: '))

if salario>1250:
    novoSalario = salario + (salario*0.1)
else:
    novoSalario = salario + (salario*0.15)

print('O salário do funcionário será R$ {:.2f}.'.format(novoSalario))