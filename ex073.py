from os import system

system ('cls')

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico - PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fotaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético - MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
system ('cls')
print(f'Lista de times do Brasileirão: {times}')
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os últimos 4 colocados são: {times[16:]}')
print(f'Times por ordem alfabética: {sorted(times)}')
posição = times.index('Chapecoense')
print(f'Chapecoense está em {posição+1}')