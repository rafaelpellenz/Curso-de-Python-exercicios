v = float(input('Qual a velocidade do carro: '))

if v >= 80:
    print('\nMULTADO!!!\n\nSerá cobrado uma multa no valor de R$ {:.2f}, por ultrapassar a velocidade de 80 km\h.'.format((v-80)*7))

print('Tenha um bom dia, dirija com segurança')