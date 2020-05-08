from datetime import datetime
maior = 0
menor = 0
data = datetime.now()

for n in range(0, 7):
    idade = int(input('Em que ano a {}ª pessoa nasceu? '.format(n+1)))
    if data.year - idade >= 18:
        maior += 1
    elif data.year - idade < 18:
        menor += 1
print('Você tem {} pessoas de maior.'.format(maior))
print('Você tem {} pessoas de menor.'.format(menor))