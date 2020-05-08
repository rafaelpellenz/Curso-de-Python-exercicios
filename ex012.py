val = float(input('Digite o valor do produto: R$ '))

desconto = val - (val*0.05)

print('Esse produto com o desconto de 5% fica no valor de R$ {:.2f}'.format(desconto))