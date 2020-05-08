num = int(input('Digite um número inteiro: '))

op = 0

for x in range(1, num+1):
    if num%x == 0:
        op += 1
if op == 2:
    print('O número {} é primo.'.format(num))
else:
    print('O {} número não é primo.'.format(num))