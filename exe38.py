#coding: utf-8

#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#* O primeiro valor é maior
#* O segundo valor é maior
#* Não existe valor maior, os dois são iguais
##################### Programa que compara números ################################################
print('\033[1;30m''/|'*10, '\033[1;33m' 'COMPARANDO NÚMEROS' '\033[m', '\033[1;30m''/|'*10, '\033[m')
print()
n1 = int(input('\033[1;30m''Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('\033[1;34m''O primeiro valor é maior')
elif n2 > n1:
    print('\033[1;35m''O segundo valor é maior')
else:
    print('\033[1;32m''Não existe valor maior, os dois são iguais')