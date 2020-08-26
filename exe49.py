#coding: utf-8

#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
   resultado = num * c
   print('{} x {:2} = {}'.format(num, c, resultado))
