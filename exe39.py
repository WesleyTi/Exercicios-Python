#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#* Se ele ainda vai se alistar ao serviço militar.
#* Se é a hora de se alistar.
#* Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

##################### PROGRAMA DE ALISTAMENTO MILITAR ######################################
from datetime import date
print('\033[1;34m''=_'*15, 'Alistamento Militar', '_='*15, '\033[m')
print('\033[1;30m')
data_nasc = str(input('Qual sua data de nascimento? '))
hoje = date.today()
print(hoje.toordinal())
