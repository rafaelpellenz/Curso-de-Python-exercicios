from os import system

system('cls')

nums = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
cont = 0

print(f'Você digitou os números {nums}')
print(f'Você digito 9, {nums.count(9)} vezes.')

if nums.count(3) > 0:
    pos = nums.index(3)
    print(f'O número 3 foi digitado na posição {pos}')
else:
    print('O número 3 não foi digitado.')

print ('Os números pares digitado ', end='')
for x in nums:
    
    if x%2 == 0:
        print(x, end=' ')
        cont += 1
if cont == 0:
    print(' foram 0')