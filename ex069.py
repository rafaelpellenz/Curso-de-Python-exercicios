from os import system

system('cls')

cont = maioresde18 = homens = mulheresmenosde20 = 0
sexo = ''

while True:
    idade = int(input('Digite a idade: '))
    while True:
        sexo = str(input("Qual é o sexo? [M/F] "))
        if sexo in 'MmFf':
            break
    cont += 1
    system('cls')

    if idade >= 18:
        maioresde18 += 1
    if sexo in 'Mm':
        homens += 1
    if idade <= 20 and sexo in 'fF':
        mulheresmenosde20 += 1

    print(f'O total de pessoas é {cont}')
    print(f'O total de pessoas com mais de 18 anos é de {maioresde18}.')
    print(f'O total de homens é {homens}.')
    print(f"O total de mulheres com menos de 20 é de {mulheresmenosde20}.")

    while True:
        op = str(input("Você quer adicionar mais pessoa? [S/N] "))
        if op in 'SsNn':
            break
    system ('cls')
    if op in 'Nn':
        break