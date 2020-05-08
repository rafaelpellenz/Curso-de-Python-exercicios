from os import system

system('cls')

primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
op = 0
resultado = primeiro

while op < 10:

    print('{} >> '.format(resultado), end = '')

    resultado += razao
    op += 1

print('FIM')