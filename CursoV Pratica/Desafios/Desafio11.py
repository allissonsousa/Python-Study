# Faça um programa que leia a largura e altura de uma parede em metros e calcule a sua área e a quantidade de tinta
# nescessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²

alt = float(input('Digite aqui em metros a altura da parede:'))
larg = float(input('Digite aqui em metros a largura da parede:'))
area = alt * larg
tinta = area / 2
print(f'Pare pintar essa parede serão nescessários {tinta:.1f} litros de tinta!')

# OUTRA FORMA QUE PODE SER FEITO
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print(f'A sua parede tem a dimensão de {alt} x {larg} e sua área é de {area}m².')
tinta = area / 2
print(f'Para pintar essa parede voce precisara de {tinta:.2f} litros de tinta!')
