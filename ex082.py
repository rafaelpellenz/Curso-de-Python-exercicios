from time import sleep
from os import system

count = 0

system ('cls')

while True:
    print(f'|  {count}%')
    sleep(0.05)
    system('cls')
    print(f'/  {count}%')
    sleep(0.05)
    system('cls')
    print(f'-  {count}%')
    sleep(0.05)
    system('cls')
    print(f'\  {count}%')
    sleep(0.05)
    system('cls')
    if count == 100:
        break
    count += 1