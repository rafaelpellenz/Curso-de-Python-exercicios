from time import sleep
import os

for c in range(10, -1, -1):
    os.system('cls') or None
    print(c)
    sleep(1)
print('\033[1;31mBOOOOMM!!\033[m')
