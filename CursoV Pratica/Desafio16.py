# Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira
# 5.123 >> 5
from math import floor
num = float(input('Digite um número real:'))
print(f'A porção inteira de {num} é {floor(num)}')
