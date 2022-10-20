from time import sleep
from random import randint #biblioteca para escolher número inteiro aleatório
print('\033[33m-=\033[m' * 10)
print('\033[33m======\033[m \033[1;32mJOKENPÔ\033[m \033[33m=====\033[m')
print('\033[33m-=\033[m' * 10)
print('''\033[32mSuas opções:
PEDRA [0]
PAPEL [1]
TESOURA [2]\033[m''')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2) #computador joga
jogador = int(input('\033[32mQual é a sua jogada?\033[m ')) #jogador joga
print('\033[1;32mJO\033[m')
sleep(1)
print('\033[1;33mKEN\033[m')
sleep(1)
print('\033[1;36mPÔ!\033[m')
sleep(1)
print('\033[32mComputador jogou\033[m \033[1;36m{}\033[m'.format(itens[computador]))
print('\033[32mJogador jogou\033[m \033[1;36m{}\033[m'.format(itens[jogador]))
if computador == 0: #computador jogou PEDRA
    if jogador == 0: #jogador jogou PEDRA
        print('\033[1;33mEMPATE!\033[m')

    elif jogador == 1: #jogador jogou PAPEL
        print('\033[1;32mVOCÊ VENCEU!\033[m')

    elif jogador == 2: #jogador jogou TESOURA
        print('\033[1;31mVOCÊ PERDEU!\033[m')

    else:
        print('\033[1;35mJOGADA INVÁLIDA!\033[m')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0: #jogador jogou PEDRA
        print('\033[1;31mVOCÊ PERDEU!\033[m')

    elif jogador == 1: #jogador jogou PAPEL
        print('\033[1;33mEMPATE!\033[m')

    elif jogador == 2: #jogador jogou TESOURA
        print('\033[1;32mVOCÊ VENCEU!\033[m')

    else:
        print('\033[1;35JOGADA INVÁLIDA!\033[m')

elif computador == 2: #computador jogou TESOURA
    if jogador == 0: #jogador jogou PEDRA
        print('\033[1;32mVOCÊ VENCEU!\033[m')

    elif jogador == 1: #jogador jogou PAPEL
        print('\033[1;31mVOCÊ PERDEU!\033[m')

    elif jogador == 2: #jogador jogou TESOURA
        print('\033[1;33mEMPATE!\033[m')

    else:
        print('\033[1;35mJOGADA INVÁLIDA!\033[m')
