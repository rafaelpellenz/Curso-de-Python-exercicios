d = float(input("Qual é a distância da sua viagem: "))

if d<=200.00:
    print('O valor da sua viagem será de R$ {:.2f}'.format(d*0.5))
else:
    print('O valor da sua viagem será de R$ {:.2f}'.format(d*0.45))