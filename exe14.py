#coding: utf-8

#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

                                # CONVERSOR DE TEMPERATURA #

c = float(input('Informe a temperatura em °C:'))
f = (9 * c) / 5 + 32
print('A temperatura de {}°C, convertida em °F é de: {}°F'.format(c, f))