""" Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um tri
ãngulo retângulo, calcule e mostre o comprimento da hipotenusa """
from math import hypot
cato = float(input('Digite aqui o comprimento do cateto oposto:'))
cata = float(input('Digite aqui o comprimento do cateto adjacente:'))
hip = hypot(cata, cato)
print(f'O comprimento da hipotenusa deste triângulo é {hip:.2f}')

# Outro método de resolução
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)  # formula do calculo sem importação
print(f'A hipotenusa vai medir {hi:.2f}')

# Método com importação de módulo
from math import hypot
cop = float(input('Comprimento do cateto oposto:'))
cad = float(input('Comprimento do cateto adjacente:'))
h = hypot(cop, cad)
print(f'A hipotenusa vai medir : {h:.2f}')
