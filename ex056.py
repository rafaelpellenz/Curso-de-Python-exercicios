nome = ''
idade = 0
sexo = ''
somaidade =0
maiorIdadeHomen = 0
nomeVelho = ''
mulheresJovens = 0
for p in range(1,5):
    print('------- {}ª PESSOA -------'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO (M/F): ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomen = idade
        nomeVelho = nome
    if idade > maiorIdadeHomen and sexo in 'Mm':
        maiorIdadeHomen = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade<20:
        mulheresJovens += 1
mediaIdade = somaidade/4
print('A média de idade do grupo é de {} anos.'.format(mediaIdade))
print('O homem mais velho do grupo é o {} e ele tem {} anos.'.format(nomeVelho, maiorIdadeHomen))
print('O número de mulheres com menos de 20 anos é {}.'.format(mulheresJovens))