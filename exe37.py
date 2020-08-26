#coding: utf-8 

#Escreva um programa que leia um número inteiro qualquer, e peça para o usuário escolher qual será a base de conversão:
#* 1 para binário
#* 2 para octal
#* 3 para hexadecimal
# ######################Programa de conversão de números##############################################
from time import sleep
print('='*10, 'Conversor de Valores', '='*10)
num = int(input('\033[1;30m''Digite um número: '))
print('\033[1;33m', 'Para conversão binária, digite 1 \n Para conversão octal, digite 2 \n Para conversão hexadecimal, digite 3 ')
resp = int(input('\033[1;30m''Digite: '))
print('\033[1;34m''Processando ...')
sleep(3)
if resp == 1:
    print('\033[1;30m''A conversão para binário é {}'.format(bin(num)))
elif resp == 2:
    print('\033[1;30m''A conversão para octal é: {}'.format(oct(num)))
elif resp == 3:
    print('\033[1;30m''A conversão para hexadecimal é: {}'.format(hex(num)))
else:
    print('\033[1;31m''Ops!!! Número errado. Digite uma das opções acima.')
