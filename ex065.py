from os import system

system('cls')

resp = op = ''
lista = []
soma = op2 = 0

while resp in 'Ss':
    while op in 'Ss':
        lista.append(int(input("Digite um valor: ")))
        op = str(input("Quer continuar [S/N]? "))
    
    soma = sum(lista)#Soma os elementos da lsta
    print(f'A média dos valores é {float(soma/len(lista)):.2f}.')
    
    lista.sort()#Ordena os elementos da lista do menor para o maior
    
    print (f'O maior valor foi {lista[len(lista)-1]} e o menor foi {lista[0]}.')
    resp = str(input("Você quer adicionar mais números? [S/N]"))
    
    if resp in 'Ss':
        op = ''
        op2 = 0