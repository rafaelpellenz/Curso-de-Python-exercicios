from os import system

system('cls')

num = int(input('Digite um número: '))

original = num
fat = num
num -= 1

while num > 0:

    fat = fat*num
    num -= 1

print ('O valor de {}! = {}'.format(original, fat))