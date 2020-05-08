from random import randint
from os import system

system('cls')

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

ordenado = sorted(tupla)
maior = ordenado[4]
menor = ordenado[0]

print (f'Os valores sorteados são: {tupla}')
print (f'O maior valor foi {maior}')
print (f'O menor valor foi {menor}')