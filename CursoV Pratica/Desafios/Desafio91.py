"""Crie um programa de 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário, no final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número dado"""
from time import sleep
from random import randint
from operator import itemgetter
"""
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

print(jogadores)
for i in range(len(jogadores)):
    contador.append(jogadores[i]['dado'])
contador.sort()
print(contador)
for c in range(len(jogadores)):
    for i in range(1, 5):
        if jogadores[i]['dado'] == contador[i]:
            print(f'{i}° lugar:{jogadores[i]['jogador']}')
            jogadores.remove(f'jogador{i}')
            jogadores.remove('dado')"""

# Não consegui resolver F

#---------------------------------------------
#Correção

jogo = {'jogador1' : randint(1, 6),
        'jogador2' : randint(1, 6),
        'jogador3' : randint(1, 6),
        'jogador4' : randint(1, 6)}

ranking = list()

print('Valores sorteados: ')
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado')
        sleep(0.7)

#IMPORTANTE !!!!!!
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)   #itemgetter 1 pega o elemento 1 do dicionario, q é o valor
                                                        # de jogador, item 0 no caso seria 'jogador', uso da chave

print('-=-' * 30)
for i, v in enumerate(ranking):
        print(f'{i + 1}° Lugar: {v[0]} com {v[1]}')

