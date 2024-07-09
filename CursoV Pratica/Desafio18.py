""" Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo"""
from math import cos, sin, tan
from fractions import Fraction
ang = int(input('Digite aqui o seu angulo:'))
c = cos(ang)
s = sin(ang)
t = tan(ang)
print(f'O ângulo de {ang} graus tem como :\n'
      f'tangente >> {t}\n'
      f'coseno >> {c}\n'
      f'seno >> {s}')
