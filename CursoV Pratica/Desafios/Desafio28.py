"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na teça se o usuário venceu ou perdeu"""
from random import random, randint, choice

n = int(choice([1, 2, 3, 4, 5]))
print('Vamos brincar !')
n0 = int(input('Tente adivinhar que número estou pensando entre 0 e 5. Qual o seu palpite ??  '))
if n == n0:
    print(f'Caramba! Como você sabia que eu estava pensando no número {n}? PARABENS!!!')
else:
    print(f'Você errou, o número q eu estava pensando era {n}. Tente mais uma vez.')

""" O choice sortea um número da lista, n recebe o valor como inteiro por causa do int"""

# CORREÇÃO

comp = randint(0, 5)
print('-=-' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 15)
jog = int(input('Em que número eu pensei ?'))
if jog == comp:
    print('Parabéns, você consguiu me vencer!')
else:
    print(f'Ganhei!! Eu pensei no número {comp}')
