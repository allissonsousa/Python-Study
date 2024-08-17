"""Faça um programa que jogue par ou impar com o computador. O jog será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo"""
from random import choice
arra = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pc = choice(arra)
print('._._' * 10)
print('VAMOS JOGAR IMPAR OU PAR')
print('._._' * 10)
jog = 11
