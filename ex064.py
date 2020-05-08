from os import system

system('cls')

soma = 0
cont = 0
op = 0

while op != 999:
    op = int(input("Digite um número [999 para parar]: "))
    if op != 999:
        soma += op
        cont += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))  