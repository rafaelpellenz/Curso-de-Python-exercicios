from random import randint
from os import system

system('cls')

vitorias = 0

while True:
    jogador = int(input('Digite um número: '))

    computador = randint(0, 10)

    pi = str(input('Você quer Par ou Impar? [P/I] '))

    total = jogador + computador

    if (total%2) == 0 and pi in 'Pp':
        print('Você ganhou.')
        vitorias += 1
    if (total%2) != 0 and pi in 'Ii':
        print('Você ganhou.')
        vitorias += 1
    if (total%2) != 0 and pi in 'Pp':
        print('Você perdeu.')
        break
    if (total%2) == 0 and pi in 'iI':
        print('Você perdeu.')
        break
print(f'Você venceu {vitorias} vezes.')
            