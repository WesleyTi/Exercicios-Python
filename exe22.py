#coding: utf-8

nome = str(input('Digite seu nome completo:')).strip()
print('Fazendo uma análise do seu nome ...')
print('Seu nome em letras maiúsculas é:{}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))# usei - nome.count(' ') para eliminar o espaço entre as palavras.
primeiro = nome.split()
print('Seu primeiro nome é {}, e ele possui {} letras'.format(primeiro[0], len(primeiro[0])))
print('Seu primeiro nome tem ao todo {} letras'.format(nome.find(' ')))# uma forma de encontrar o primeiro nome usando ' ' espaço no find()