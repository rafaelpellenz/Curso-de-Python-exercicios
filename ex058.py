import keyboard
import string
from threading import *


#Optional code(extra keys):

#keys.append("space_bar")
#keys.append("backspace")
#keys.append("shift")
#keys.append("esc")


# Atribuo a lista de caracteres ascii para a variavel keys(não encontrei lista com todas as teclas)
teclas = list(string.printable)

def listen(tecla):
    while True:
        keyboard.wait(tecla)
        print("- Tecla pressionada: ",tecla)
threads = [Thread(target=listen, kwargs={"tecla":tecla}) for tecla in teclas]

for thread in threads:
    thread.start()