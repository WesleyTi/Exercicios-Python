#coding: utf-8

#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.

                            # Desconto no produto #

preco = float(input('Informe o preço do produto: R$'))
desc = (preco * 5)/100
print('O produto com 5% de desconto sai por: R${:.2f}'.format(preco - desc))
