from datetime import datetime

agora = datetime.now()

idade = int(input('Em que ano você nasceu: '))

if (agora.year-idade) > 17:
    print('O seu prazo de alistamento expirou a {} anos'.format((agora.year-idade)-17))
elif (agora.year-idade) < 17:
    print('Ainda faltam {} anos para o seu alistamento.'.format(17-(agora.year-idade)))
elif (agora.year-idade) == 17:
    print('Você deve se alistar, procure a junta militar mais próxima de você')
