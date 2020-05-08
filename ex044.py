preco = float(input('Preço do produto: R$ '))

print('Forma de pagamento?')
print('1- Dinheiro ou cheque')
print('2- Cartão')
op1 = int(input("Digite a opção e tecle ENTER: "))

if op1 == 1:
    print('O total é de R$ {:.2f}'.format(preco-(preco*0.1)))
elif op1 == 2:
    print('O pagamento será parcelado ou à vista?')
    print('1- Pagamento à vista')
    print('2- Pagamento parcelado')
    op2 = int(input('Digite a Opção e tecle ENTER: '))

    if op2 == 1:
        print('O total é de R$ {:.2f}'.format(preco-(preco*0.05)))
    elif op2 == 2:
        numParcelas = int(input('Digite a quantia de parcelas e tecle ENTER: '))
        if numParcelas<=2:
            print('O total é de R$ {:.2f}'.format(preco))
        elif numParcelas>2:
            print('O preço total é de R$ {:.2f}'.format(preco+(preco*0.2)))