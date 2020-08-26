#coding: utf-8

#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.
from datetime import date # importando biblioteca de data
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual:  '))
if ano == 0: # atribuindo 0 para o ano atual
    ano = date.today().year# atribuindo 0 para o ano atual.
print('Analisando se ele é bissexto...')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {}, é ano bissexto'.format(ano))
else:
    print('O ano de {}, não é ano bissexto'.format(ano))