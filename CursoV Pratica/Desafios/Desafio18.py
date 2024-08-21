""" Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo"""

from math import cos, sin, tan, radians
ang = int(input('Digite aqui o seu angulo:'))
c = cos(ang)
s = sin(ang)                                    # O erro aqui é q eu nao sabia q o grau q o python usa é radiano n graus
t = tan(ang)
print(f'O ângulo de {ang} graus tem como :\n'
      f'tangente >> {t:.2f}\n'
      f'coseno >> {c:.2f}\n'
      f'seno >> {s:.2f}')

# Correção
an = float(input('Digite o angulo que você deseja:'))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print(f'O ângulo de {an} tem o Seno de {seno:.2f}\n'
      f'O ângulo de {an} tem o Cosseno de {cosseno:.2f}\n'
      f'O ângulo de {an} tem a Tangente de {tangente:.2f}')
# conversão da medida em radianos para graus e depois para seno
