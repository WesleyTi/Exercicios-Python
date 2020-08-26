#coding: utf-8

#ESCREVA UM PROGRAMA QUE PERGUNTE O SÁLARIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
#* PARA SALÁRIOS SUPERIORES A R$1.250,00, CALCULE UM AUMENTO DE 10%.
#* PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.
##### Programa Salário #####
salario = float(input('Informe o valor do salário: R$'))
if salario > 1250.00:
    aumento = salario*10/100
else:
    aumento = salario*15/100
print('O salário de R${:.2f}, teve um reajuste de R${:.2f}, totalizando o valor de R${:.2f}'.format(salario, aumento, salario + aumento))