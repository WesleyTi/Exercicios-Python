#coding: utf-8

#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE  NA TELA A SUA PORÇÃO INTEIRA.

#1ª forma de fazer usando módulos.
from math import trunc
num_real = float(input('Digite um número real:'))
print('O número real {} tem a sua porção inteira de {}'.format(num_real, trunc(num_real)))
# math.trunc()... me mostra somente o número inteiro.

# 2ª forma de fazer sem importar módulos e usando int na formatação
'''num_real = float(input('Digite um número real:'))
print('O número real {} tem a sua porção inteira de {}'.format(num_real, int(num_real)))'''