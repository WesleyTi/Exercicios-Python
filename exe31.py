#coding: utf-8

#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$ 0,45 PARA VIAGENS MAIS LONGAS.

distancia = float(input('Informe a distância em Km: '))
'''if distancia <= 200:
    print('O valor para passagens até 200Km rodados, ficou em: R${:.2f}'.format((distancia*0.50)))
else:
    print('O valor para passagens acima de 200Km rodados, ficou em: R${:.2f}'.format(distancia*0.45))'''
# condição simplificada...
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor da sua passagem será: R${:.2f}'.format(preco))