#coding: utf-8

#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO.
from random import choice

n1 = input('Informe o nome do primeiro aluno:')
n2 = input('informe o nome do segundo aluno:')
n3 = input('Informe o nome do terceiro aluno:')
n4 = input('Informe o nome do quarto aluno:')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O sorteado para apagar o quadro foi: {}'.format(escolhido))
