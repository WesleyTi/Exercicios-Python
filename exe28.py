#coding: utf-8

#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0 E 5, E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
#* O computador deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep# função tempo ...
computador = randint(0, 5)# faz o computador pensar...
print('====== Jogo da advinhação ======')
print('O computador vai escolher um número...')
jogador = int(input('Tente a sorte agora... Digite um número de 0 a 5: '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns !!! Você ganhou...O número escolhido pelo computador foi {}'.format(computador))
else:
    print('Que pena!!! Não foi desta vez.')
    print('O número escolhido pelo computador foi {}.'.format(computador))