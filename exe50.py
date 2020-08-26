#coding: utf-8

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
print()
print('{:^}'.format('Somando números pares.'))
print()
soma = 0
subtrair = 0
for c in range(1, 7):
   num = int(input('Digite um valor: '))
   if num != num % 2 == 0:
       soma = num + soma
   elif num == num % 3 == 0:
       subtrair = num - subtrair
print('A soma do números pares é {}'.format(soma))