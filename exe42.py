#coding: utf-8

#Refaça o desafio 035 dos triângulos,
#acrescentando o recurso de mostrar que tipo de triângulo será formado:
#* Equilátero: todos os lados iguais
#* Isósceles: dois lados iguais
#* Escaleno: todos os lados diferentes

print('\033[7;30m''[\_/]'*5, 'Analisador de triângulos', '[\_/]'*5, '\033[m')
print('\033[1;34m')
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 == r2 == r3:
    print('\033[1;30m''As retas {:.1f}, {:.1f} e {:.1f}, formam um triângulo:''\033[m''\033[7;30m'' EQUILÁTERO ''\033[m'.format(r1, r2, r3))
elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
    print('\033[1;30m''As retas {:.1f}, {:.1f} e {:.1f}, formam um triângulo:''\033[m''\033[7;30m'' ISÓSCELES ''\033[m'.format(r1, r2, r3))
else:
    print('\033[1;30m''As retas {}, {} e {}, formam um triângulo:''\033[m''\033[7;30m'' ESCALENO ''\033[m'.format(r1, r2, r3))