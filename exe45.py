#coding: utf-8

#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

print('\033[1;32m''?\/?'*8, '\033[1;34m''Que comecem os Jogos !!! Jokenpô !', '\033[1;32m''?\/?'*8, '\033[1;32m')
print()
print(' '*22, '\033[1;30m''='*50)
print('\033[1;30m''='*100)
opções = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Faça sua escolha... 
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura ''')
jogador = int(input('Sua jogada: '))
if jogador > 2:
    print('\033[1;31m''OPÇÃO INVÁLIDA !!!''\033[m')
else:
    print('\033[1;33m'' '*7, 'JO')
    sleep(1)
    print(' '*7, 'KEN')
    sleep(1)
    print(' '*7, 'PÔ!!!!''\033[m')
    sleep(0.5)
    print('='*20, '\033[1;36m')
    print('\033[1m''Computador jogou {}'.format(opções[computador]))
    print('Você jogou {}'.format(opções[jogador]))
    print('='*20, '\033[1;36m')
if computador == 0:# computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU !!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU !!!')

elif computador == 1:# computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU !!!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU !!!')

elif computador == 2:# computador jogou tesoura
    if jogador == 0:
        print('VOCÊ VENCEU !!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU !!!')
    elif jogador == 2:
        print('EMPATE')