#coding: utf-8

#FAÇA UM ALGORITMO QUE LEIA O SÁLARIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SÁLARIO COM 15% DE AUMENTO.

                            # Aumento de sálario #

sal = float(input('Informe o sálario do funcionário: R$'))
acres = (sal * 15 / 100)
print('O novo sálario do funcionário com 15% de aumento é R${:.2f}'. format(sal + acres))
print('Uma diferença de R${:.2f} para o sálario anterior.'.format(acres))