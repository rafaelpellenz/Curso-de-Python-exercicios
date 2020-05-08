import math

ca = float(input('Comprimento do cateto adjacente: '))
co = float(input('Comprimento do cateto oposto: '))

hip = math.hypot(ca, co)

print('A hipotenusa vai medir {:.2f}'.format(hip))
