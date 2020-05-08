import random
import time

print('*'*45)
print('** Tente adivinhar o número entre 0 e 5!!! **')
print('*'*45)

computador = random.randint(0,5)

jogador = int(input('\nDigite um número de 0 a 5: '))

print('PROCESSANDO...')
time.sleep(3)

if computador == jogador:
    print('Você acertou!!!')
else:
    print('Você errou, o número era {}.'.format(computador))