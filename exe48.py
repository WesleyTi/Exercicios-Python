#coding: utf-8

#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.
import math
cont = 0 # contador
soma = 0 # acumulador
for c in range(1, 501, 2):# pra mostrar os números impáres, comecei do 1 até 501, pulando de 2 em 2... assim vai me mostrar todos números impáres.
   if c % 3 == 0:
       cont = cont + 1 # é um contador, por isso adicionei + 1
       soma = soma + c # é um acumulador de números
       #print(c, end=' ')# end =' ' deixa espaço entre os números e os coloca em linha horizontal.
print(' A soma de todos {} números ímpares, múltiplos de três são: {}'.format(cont, soma))