from os import system

system('cls')

soma = cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    cont+=1
    soma = soma + n
system('cls')
print(f'Você digitou {cont} números e a soma total deles é {soma}.')