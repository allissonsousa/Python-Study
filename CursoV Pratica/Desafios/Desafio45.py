"""Crie um programa que faça o computador jogar Jokennpo com voce"""
from random import choice, randint
from time import sleep
'''n = str(choice(['Tesoura', 'Papel', 'Pedra']).upper())  # lista com os nomes, choice faz o sorteio
mao = str(input('JO KEN PO!\n').upper())  # o upper usa pra nao dar erro caso o usuario digite de uma forma diferente
if mao == n:
    print(f'{n}!!!\nQue coincidencia, estamos pensando igual, vamos tentar denovo!')
elif mao == 'PEDRA' and n == 'TESOURA':
    print(f'{n}!!!\nOH não, você mostrou {mao} e ganhou. Parabéns!')
elif mao == 'TESOURA' and n == 'PAPEL':
    print(f'{n}!!!\nOH  não, você mostrou {mao} e ganhou. Parabéns!')
elif mao == 'PAPEL' and n == 'PEDRA':
    print(f'{n}!!!\nOh não, você mostrou {mao} e ganhou. Parabéns!')
else:
    print(f'{n}!!!\nEbaaa, você mostrou {mao} e perdeu. Tente denovo.')'''

# CORREÇÃO
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)
print('-=-' * 10)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=-' * 10)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('JOGADA INVÁLIDA')