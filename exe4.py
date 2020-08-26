# coding: utf-8
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

m = str(input('Digite 2 letras e 2 números:'))
print(type(m))
print(m.isupper())
print(m.istitle())
print(m.isspace())
print(m.isnumeric())
print(m.islower())
print(m.isidentifier())
print(m.isdigit())
print(m.isdecimal())
print(m.isalpha())
print(m.isalnum())
print(m.isprintable())
