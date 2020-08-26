#coding: utf-8

#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#* Média abaixo de 5.0:
#REPROVADO
#*Média entre 5.0 e 6.9:
#RECUPERAÇÂO
#*Média 7.0 ou superior:
#APROVADO
print('\033[1;30m''*_-'*10, 'Notas dos Alunos','*_-' *10)
print()
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
média = (n1 + n2) / 2
print('A soma das {:.1f} e {:.1f} tem a média {:.1f}'.format(n1, n2, média))
print('O aluno está: ')
if média < 4.99:
    print('\033[1;31m''REPROVADO''\033 [m')
elif média < 7.0:
    print('\033[1;33m''RECUPERAÇÃO''\033[m')
else:
    print('\033[1;32m''APROVADO''\033[m')