#coding: utf-8 

#Faça um programa que leia uma frase pelo teclado e mostre:
#* Quantas vezes aparece a letra "A".
#* Em que posição ela aparece a primeira vez.
#* Em que posição aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece:{}'.format(frase.count('A')))
print('A posição que ela aparece a primeira vez, é a: {}ª'.format(frase.find('A')+1))# adicionei +1 para não me mostrar a posição 0
print('A última posição da letra A é: {}ª'.format(frase.rfind('A')+1))# adicionei +1 para para o usuário a posição que a tela mostra, não a que o Python entende... ex: bbba = seria para o python a posição 3, e para o usuário 4... por isso foi adicionado o +1
