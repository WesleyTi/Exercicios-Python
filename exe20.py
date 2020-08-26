#coding: utf-8

#O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.
from random import shuffle # shuffle embaralha a ordem
n1 = input('Aluno 1:')
n2 = input('Aluno 2:')
n3 = input('Aluno 3:')
n4 = input('Aluno 4:')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação de trabalho será:\n {}'.format(lista))