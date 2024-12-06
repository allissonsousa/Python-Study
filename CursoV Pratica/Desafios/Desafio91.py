"""Crie um programa de 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário, no final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número dado"""
from time import sleep
from random import randint
jogadores = list()
jogador = dict()
contador = list()

print('Valores sorteados: \n')
for i in range(1, 5):
    dado = randint(1, 6)
    print(f'O jogador {i} tirou {str(dado)} no dado')
    jogador['jogador'] = f'jogador{i}'
    jogador['dado'] = dado
    jogadores.append(jogador.copy())
    sleep(0.7)
for i in range(len(jogadores)):
    contador.append(jogadores[i]['dado'])
contador.sort()
print(contador)
for c in range(len(jogadores)):
    for i in range(0, 4):
        if jogadores[i]['dado'] == contador[i]:
            print(f'{i}° lugar:{jogadores[i]['jogador']}')

