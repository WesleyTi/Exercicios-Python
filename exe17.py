#coding: utf-8

#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

# 1ª resolução do programa sem módulos
'''c_o = float(input('Informe o comprimento do cateto oposto:'))
c_a = float(input('Informe o comprimento do cateto adjacente:'))
h = (c_o**2 + c_a**2) / (1/2)
print('A hipotenusa do triângulo vai medir : {:.2f}'.format(h))'''

# 2ª resolução do programa com módulos
from math import hypot# Importando a função hipotenusa
c_o = float(input('Informe o comprimento do cateto oposto:'))
c_a = float(input('Informe o comprimento do cateto adjacente:'))
h = hypot(c_o, c_a)
print('A hipotenusa do triângulo vai medir: {:.2f}'.format(h))