"""Faça um programa que ajuda um jogador da Mega sena a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta"""
from random import randint
from time import sleep

jogo = []
composta = []
print('==' * 20)
print(f'APOSTA DO TIGRINHO'.center(40))
print('==' * 20)
quantos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'SORTEANDO {quantos} JOGOS'.center(40, '='))
for i in range(0, quantos):
    while len(jogo) < 6:
        val = randint(1, 60)
        if val not in jogo:
            jogo.append(val)
    jogo.sort()
    composta.append(jogo[:])
    jogo.clear()

for i in range(0, quantos):
    print(f'JOGO {i + 1}: {composta[i]}')
    sleep(0.7)

print('-=-' * 10)

