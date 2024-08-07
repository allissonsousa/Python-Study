""" Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um número de 0 a 10 . Só que agora o jogador
vai tentar adivinhar, até acertar, mostrando no final quantos palpites foram necessários para vencer"""
from random import choice
comp = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
jog = 0
palp = 0
print('--------------- JOGO DA ADIVINHA -----------------')
while comp != jog:
    jog = int(input('Em qual número você acha que eu estou pensando de 0 a 10 ?\n'))
    palp += 1
    if comp != jog:
        print('\033[31mERROU!!!\033[m estou pensando em outro número. Tente novamente!\n')
print(f'\033[36mPARABÉNS!!!!!\033[m eu estava pensando no número {comp}\n'
      f'Você conseguiu adivinhar só com {palp} tentativas, muito bom.')