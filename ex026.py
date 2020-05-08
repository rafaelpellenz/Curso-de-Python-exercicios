frase = str(input('Digite uma frase: ')).lower()

n = frase.strip()

print('A letra "A" aparece {} vezes na frase.'.format(n.count('a')))
print('O primeiro "A" aparece na posição {}.'.format(n.find('a')+1))
print('O segundo "A" aparece na posição {}'.format(n.rfind('a')+1))