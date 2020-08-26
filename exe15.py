#coding: utf-8

#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias, pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.

                                # ALUGUEL DE CARRO #

km = float(input('Informe os Km percorridos:'))
dias = int(input('Quantos dias ficou alugado?'))
preco = dias * 60 + km * 0.15
print('O valor total do aluguel é de R${:.2f}'.format(preco))
