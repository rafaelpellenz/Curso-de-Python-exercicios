dias = int(input('Digite o número de dias: '))
km = float(input("Digite quantos km o carro rodou: "))

custoDiaria = dias * 60
custoKm = km * 0.15
valorTotal = custoKm + float(custoDiaria)

print('O valor a ser cobrado é de R$ {:.2f}'.format(valorTotal))