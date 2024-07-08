""" Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um tri
ãngulo retângulo, calcule e mostre o comprimento da hipotenusa """
from math import hypot
cato = int(input('Digite aqui o comprimento do cateto oposto:'))
cata = int(input('Digite aqui o comprimento do cateto adjacente:'))
hip = hypot(cata, cato)
print(f'O comprimento da hipotenusa deste triângulo é {hip:.2f1}')