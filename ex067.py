from os import system
system('cls')
x=0
while True:
    print('*'*37)
    print('* Quer ver a tabuada de qual valor? * ')
    print('*'*37)
    n = int(input())
    if n < 0:
        break
    print('\n')
    for x in range(11):
        print(f'{n} X {x} = {n*x}')
print("Programa encerrado.")