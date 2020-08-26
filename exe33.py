#coding: utf-8

#FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E O MENOR.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
# Verificando qual é maior valor:
maior = n1
if n2>n3 and n2>n1:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

# Verificando o menor valor:
menor = n1
if n2<n3 and n2<n1:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))
