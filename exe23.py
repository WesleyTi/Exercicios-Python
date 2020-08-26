#coding: utf-8

"""<numero = input('Digite um número de 0 a 9999:')
separado = numero.split()
print('Unidade:{}'.format(separado[0][0]))
print('Dezena:{}'.format(separado[0][1]))
print('Centena:{}'.format(separado[0][2]))
print('Milhar:{}'.format(separado[0][3]))""" # o código que eu fiz.../>

"""numero = int(input('Digite um número:'))
num = str(numero)
print('Analisando o número {}...'. format(numero))
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'. format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))""" # código do Guanabara

# Ambos os códigos funcionam para números de 4 unidades ... ex 1986
# usando menos que isso o programa da erro.
# O código a seguir usa a lógica matemática para resolver o problema.

numero = int(input('Digite um número:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))