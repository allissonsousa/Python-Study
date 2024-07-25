"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na teça se o usuário venceu ou perdeu"""
import random

n = int(random.choice([1, 2, 3, 4, 5]))
print('Vamos brincar !')
n0 = int(input('Tente adivinhar que número estou pensando. Qual o seu palpite ??  '))
if n == n0:
    print(f'Caramba! Como você sabia que eu estava pensando no número {n}? PARABENS!!!')
else:
    print(f'Você errou, o número q eu estava pensando era {n}. Tente mais uma vez.')

""" O random.choice sortea um número da lista, n recebe o valor como inteiro por causa do int"""
