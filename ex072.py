nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sate', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    x = int(input('Digite um um número entre 0 e 20: '))
    if x >= 0 and x <= 20:
        print(f"Você digitou o número {nums[x]}.")
        break
    print('Tente novamente. ', end='')