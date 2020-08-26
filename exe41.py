#coding: utf-8 

#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de carodo com a idade:
#* Até 9 anos: MIRIM
#* Até 14 anos: INFANTIL
#* Até 19 anos: JUNIOR
#* Até 20 anos: SÊNIOR
#* Acima: MASTER
from datetime import date
print('\033[1;34m''|\_'*5, '\033[m' '\033[1;30m''Tabela de categoria da Federação Nacional de Natação', '\033[1;34m''_/|'*5, '\033[m')
print()
data_nasc = int((input('\033[1;30m''Informe o ano de nascimento do atleta: ')))
hoje = date.today().year
idade = hoje - data_nasc
print()
print('\033[1;34m''  Até 9 anos de idade: MIRIM \n  Até 14 anos: INFANTIL \n  Até 19 anos: JUNIOR \n  Até 20 anos: SÊNIOR \n  Acima de 20 anos: MASTER''\033[m')
print('\033[1;30m')
if idade <= 9:
    print('A categoria do atleta de {} anos, é a: MIRIM'.format(idade))
elif idade <= 14:
    print('A categoria do atleta de {} anos, é a: INFANTIL'.format(idade))
elif idade <= 19:
    print('A categoria do atleta de {} anos, é a: JUNIOR '.format(idade))
elif idade == 20:
    print('A categoria do atleta de {} anos, é a: SÊNIOR'.format(idade))
else:
    print('A Categoria do atleta de {} é a: MASTER'.format(idade))