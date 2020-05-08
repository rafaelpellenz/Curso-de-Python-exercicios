x = int(input('Digite um número inteiro: '))
print('Escolha o formato para conversão')
print('\n\033[31m1-\033[m Binário')
print('\033[31m2-\033[m Octal')
print('\033[31m3-\033[m Hexadecimal\n')
menu = int(input('Digite o número da opção e tecle ENTER: '))

b = bin(x)
o = oct(x)
h = hex(x)

if menu == 1:
    print('O valor {} em binário é {}.'.format(x, b[2:]))
elif menu == 2:
    print('O valor {} em octael é {}'.format(x, o[2:]))
elif menu == 3:
    print('O valor {} em hexadecimal é {}'.format(x, h[2:]))

print('''
*********************************
**           fim               **
*********************************''')