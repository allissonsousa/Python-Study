"""Crie um programa que faça o computador jogar Jokennpo com voce"""
from random import choice
n = str(choice(['Tesoura', 'Papel', 'Pedra']).upper())  # lista com os nomes, choice faz o sorteio
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
    print(f'{n}!!!\nEbaaa, você mostrou {mao} e perdeu. Tente denovo.')
