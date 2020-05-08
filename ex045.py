import emoji
import time
import random

op = ['Pedra', 'Papel', 'Tesoura']

print('*'*15)
print('**  \033[1;31mJOKENPO\033[m  **')
print('*'*15)
print('\n')

computador = random.choice(op)

print('Escolha Pedra, Papel ou Tesoura:')
print('1- Pedra')
print('2- Papel')
print('3- Tesoura')
op2 = int(input('Digite o número da opção e tecle ENTER: '))

if op2 == 1:
    jogador = op[0]
elif op2 == 2:
    jogador = op[1]
elif op2 == 3:
    jogador = op[2]

print('\033[1;31mJO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO\033[m')

if jogador =='Pedra' and computador == 'Pedra':
    print(emoji.emojize('\033[1mJOGADOR :oncoming_fist: X :oncoming_fist: COMPUTADOR\033[m'))
    print('Empate')

elif jogador == 'Pedra' and computador == 'Papel':
    print(emoji.emojize('\033[1mJOGADOR :oncoming_fist: X :raised_hand: COMPUTADOR\033[m'))
    print('Perdeu')

elif jogador == 'Pedra' and computador == 'Tesoura':
    print(emoji.emojize('\033[1mJOGADOR :oncoming_fist: X :victory_hand: COMPUTADOR\033[m'))
    print('Ganhou')

elif jogador == 'Papel' and computador == 'Pedra':
    print(emoji.emojize('\033[1mJOGADOR :raised_hand: X :oncoming_fist: COMPUTADOR\033[m'))
    print('Ganhou')

elif jogador == 'Papel' and computador == 'Papel':
    print(emoji.emojize('\033[1mJOGADOR :raised_hand: X :raised_hand: COMPUTADOR\033[m'))
    print('Empate')

elif jogador == 'Papel' and computador == 'Tesoura':
    print(emoji.emojize('\033[1mJOGADOR :raised_hand: X :victory_hand: COMPUTADOR\033[m'))
    print('Perdeu')

elif jogador == 'Tesoura' and computador == 'Pedra':
    print(emoji.emojize('\033[1mJOGADOR :victory_hand: X :oncoming_fist: COMPUTADOR\033[m'))
    print('Perdeu')

elif jogador == 'Tesoura' and computador == 'Papel':
    print(emoji.emojize('\033[1mJOGADOR :victory_hand: X :raised_hand: COMPUTADOR\033[m'))
    print('Ganhou')

elif jogador == 'Tesoura' and computador == 'Tesoura':
    print(emoji.emojize('\033[1mJOGADOR :victory_hand: X :victory_hand: COMPUTADOR\033[m'))
    print('Empate')