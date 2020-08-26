#coding: utf-8

#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
#* SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
#* A MULTA VAI CUSTAR R$ 7,00 POR CADA KM ACIMA DO LIMITE.
from random import randint
print(35*'=')
print('Velocidade máxima permitida: 80km/h')
print('Recebendo a velocidade do veículo...')
#velocidade = int(input(''Recebendo a velocidade do veículo...'))
velocidade = randint(60, 200)
if velocidade <= 80:
    print('O veículo está a {}km. Velocidade permitida'.format(velocidade))
else:
    print('Seu veículo  passou a {}km/h, e foi multado em: {}'.format(velocidade, (velocidade - 80)*7))