from os import system

system('cls')

termos = int(input("Número de termos: "))

n1 = 0
n2 = 1
n3 = 0
op = 0

while op < termos:

    print (n1, end= ' >> ')

    n3 = n2+n1
    n1 = n2
    n2 = n3



    op += 1

print('FIM')