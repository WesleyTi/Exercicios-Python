#coding: utf-8

#FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO.
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno do ângulo de {:.2f}º, é: {:.2f}'.format(angulo, seno))
print('O cosseno do ângulo de {:.2f}º, é: {:.2f}'.format(angulo, cosseno))
print('A tangente do ângulo de {:.2f}º, é: {:.2f}'.format(angulo, tangente))