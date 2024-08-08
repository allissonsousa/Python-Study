""" Refaça o Desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão,
usando a estrutura while"""
pri = int(input('Digite aqui o primeiro termo da sua PA: '))
ra = int(input('Digite aqui a razão da sua PA: '))
pa = pri + (10 * ra)
termo = pri
while termo != pa:
    termo += ra
    print(termo)