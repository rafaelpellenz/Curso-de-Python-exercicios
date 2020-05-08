from os import system

system('cls')

menorvalor = mil = soma = 0

while True:
    nome = str(input("Nome do produto: "))
    preço = float(input('Preço do produto: R$ '))

    soma = soma + preço

    if preço >= 1000.00:
        mil += 1
    
    if menorvalor == 0:
        nomebarato = nome
        menorvalor = preço
    if menorvalor > preço:
        nomebarato = nome
        menorvalor = preço
    
    while True:
        op = str(input("Você quer adicionar mais um produto? [S/N] "))
        if op in 'SsNn':
            break
    if op in 'Nn':
        break

print(f'O tota da compra foi R$ {soma}.')
print(f"{mil} produtos custaram mais de R$ 1000,00.")
print(f'O produto mais barato foi {nomebarato} e custou R$ {menorvalor:.2f}')