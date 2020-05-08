a = float(input("Digite o valor da reta 1: "))
b = float(input("Digite o valor da reta 2: "))
c = float(input("Digite o valor da reta 3: "))

if abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b:
    print('Você consegue formar um triangulo com essas retas.')
else:
    print('Você não consegue formar um triângulo com essas retas.')