#coding: utf-8

#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa entre eles.
from time import sleep

print('\033[1;30m''#%_@'*50)
print()
print('{:^}'.format('\033[1;31m''CONTAGEM REGRESSIVA PARA QUEIMA DE FOGOS DE ARTIFÍCIO.'))
print()
print('\033[1;30m''#%_@'*50)
for c in range(10, 0, -1):
   sleep(1)
   print()
   print('\033[1;33m''{:^50}'.format(c))
   print()
print(' '*15, 'Cabummmmmmmm!!!!!')
