#coding: utf-8

#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.
#(US$ 1,00 = R$ 3,27)
#                           CONVERSOR DE MOEDAS
d = float(input('Digite a quantia de dinheiro que possuem na carteira  R$'))
c = d / 3.27
print('Com essa quantia de R${:.2f} reais, você pode comprar US${:.2f} dólares.'.format(d, c))