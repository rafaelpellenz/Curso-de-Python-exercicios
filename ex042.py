a = float(input("Digite o valor da reta 1: "))
b = float(input("Digite o valor da reta 2: "))
c = float(input("Digite o valor da reta 3: "))

if abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b:
    if a==b and a==c:
        triangulo = 'Equilátero'
    elif (a==b or a==c and b!=c) or (b==a or b==c and a!=c) or (c==b or c==a and a!=b):
        triangulo = 'Isóceles'
    elif a!=b and a!=c and b!=c:
        triangulo = 'Escaleno'
    print('Você consegue formar um triangulo {} com essas retas.'.format(triangulo))
else:
    print('Você não consegue formar um triângulo com essas retas.')