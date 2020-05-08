from os import system

system ('cls')
saque = int(input("Quanto você quer sacar? R$ "))
total = saque
cedula = 50
totcedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        totcedulas += 1
    else:
        if totcedulas > 0:
            print (f'Total de {totcedulas} notas de R$ {cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula =1
        totcedulas = 0
        if total == 0:
            break
#cinquenta = int(saque/50)
#vinte = int((saque%50)/20)
#dez = int(((saque%50)%20)/10)
#um = int((((saque%50)%20)%10)/1)

#if cinquenta > 0:
#    print (f'Total de {cinquenta} notas de R$ 50,00.')
#if vinte > 0:
#    print (f'Total de {vinte} notas de R$ 20,00.')
#if dez > 0:
#    print (f'Total de {dez} notas de R$ 10,00.')
#if um > 0:
#    print (f'Total de {um} notas de R$ 1,00.')