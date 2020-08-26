#coding: utf-8

#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA. SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2m².

                            # Pintando parede #
larg = float(input('Digite a largura da parede em m²:'))
alt = float(input('Digite a altura da parede em m²:'))
area = larg * alt
#litro = calc / 2
print('A dimensão da parede é de {} x {} e sua área total é de {} m² '.format(larg, alt, area))
print('Será necessário {:.2f} litros de tinta para pinta-la.'.format(area / 2))