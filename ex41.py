print('\033[36m*'*31)
print('\033[36m**  \033[1mClassificador de atleta\033[0;36m  **')
print('\033[36m*\033[m'*31)

idade = int(input('Qual é a idade do atleta: '))

if idade < 9:
    print('\033[1;31mMIRIM\033[m')
    print('INFANTIL')
    print('JUNIOR')
    print('SÊNIOR')
    print('MASTER')
elif idade>=9 and idade<14:
    print('MIRIM')
    print('\033[1;31mINFANTIL\033[m')
    print('JUNIOR')
    print('SÊNIOR')
    print("MASTER")
elif idade>=14 and idade<19:
    print('MIRIM')
    print('INFANTIL')
    print('\033[1;31mJUNIOR\033[m')
    print('SÊNIOR')
    print('MASTER')
elif idade>=19 and idade<20:
    print('MIRIM')
    print('INFANTIL')
    print('JUNIOR')
    print('\033[1;31mSÊNIOR\033[m')
    print('MASTER')
elif idade>20:
    print('MIRIM')
    print('INFANTIL')
    print('JUNIOR')
    print('SÊNIOR')
    print('\033[1;31mMASTER\033[m')