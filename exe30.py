#coding: utf-8

#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR.
print('-='*20)
print('Verificando números pares e ímpares.')
print('-='*20)
numero = int(input('Digite um número: '))
if (numero % 2) == 0:
    print('O número {}, é par'.format(numero))
else:
    print('O número {}, é impar.'.format(numero))
print('=-'*20)