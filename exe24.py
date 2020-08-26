#coding: utf-8

#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

"""nome = str(input('Digite o nome de uma cidade:')).strip()
primeiro_nome = nome.upper().split()
print('SANTO' in primeiro_nome[0])""" # meu código

# O Código do Guanabara

nome_cidade = str(input('Digite o nome de uma cidade:')).strip()
print(nome_cidade[:5].upper() == 'SANTO')# nome_cidade[:5], me mostra baseado na quantidade de letras a palavra santo tem (5) e : não preciso indicar o começo
