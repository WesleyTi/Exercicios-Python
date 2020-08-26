#coding: utf-8

#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#* Abaixo de 18.5: Abaixo do peso
#* Entre 18.5 e 25: Peso ideal
#* 25 até 30: Sobrepeso
#* 30 até 40: Obesidade
#* Acima de 40: Obesidade mórbida

print('\033[1;30m''¨¨_¨¨'*5, 'Consulte seu IMC, e saiba seu status de peso.', '¨¨_¨¨'*5)
print()
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / altura**2
print('='*35)
print('\033[1;32m'' Abaixo de 18.5: Abaixo do peso\n'
      ' Entre 18.5 e 25: Peso ideal\n'
      '       25 até 30: Sobrepeso\n'
      '       30 até 40: Obesidade\n'
      ' Acima de 40: Obesidade mórbida''\033[m')
print('='*35, '\033[1;30m')
print()
if imc < 18.5:
    print('Seu imc é de {:.1f}. ''\033[1;36m''Você está abaixo do peso.''\033[m'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu imc é de {:.1f}.''\033[1;36m'' Você está com peso normal.''\033[m'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu imc é de {:.1f}.''\033[1;36m''Você está com sobrepeso.''\033[m'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu imc é de {:.1f}.''\033[1;36m''Você está com obesidade.''\033[m'.format(imc))
else:
    print('Seu imc é de {:.1f}.''\033[1;36m''Você está com obesidade mórbida'.format(imc))