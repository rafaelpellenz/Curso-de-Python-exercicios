from os import system
from time import sleep

op=0

system ('cls')

n1 =  int(input('Digite o primeiro valor: '))
n2 =  int(input('Digite o segundo valor: '))

system('cls')

while op != '5':
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair''')

    op = str(input('Escolha uma opção: '))

    if op == '1':
        print('{} + {} = {}'.format(n1, n2, n1+n2))
        input('Aperte ENTER para voltar ao menu.')
        system('cls')

    if op == '2':
        print('{} X {} = {}'.format(n1, n2, n1*n2))
        input('Aperte ENTER para voltar ao menu.')
        system('cls')

    if op == '3':
        if n1 > n2:
            print('{} é o maior'.format(n1))
        if n1 < n2:
            print('{} é o maior'.format(n2))
        elif n1 == n2:
            print('{} e {} são iguais'.format(n1, n2))        
        input('Aperte ENTER para voltar ao menu.')
        system('cls')

    if op == '4':
        n1 =  int(input('Digite o primeiro valor: '))
        n2 =  int(input('Digite o segundo valor: '))
        input('Aperte ENTER para voltar ao menu.')
        system('cls')
    if op == '5':
        print('Até logo.')
        sleep(2)
    else:
        print('Opção inválida')
        sleep (2)
        system('cls')