n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

if media < 5.0:
    print('\033[1;31mREPROVADO')
elif media >= 5.0 and media < 7.0:
    print('\033[1;33mRECUPERAÇÃO')
elif media >= 7.0:
    print('\033[1;32mAPROVADO')