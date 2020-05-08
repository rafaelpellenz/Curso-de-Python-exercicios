from os import system

system('cls')

primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
op = 0
numTermos = 10
termos = 10
resultado = primeiro

while termos != 0:
    while op < termos:

        print('{} >> '.format(resultado), end = '')

        resultado += razao
        op += 1

    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar a mais? '))
    numTermos += termos
    op = 0

print('O total de termos foi {}'.format(numTermos))