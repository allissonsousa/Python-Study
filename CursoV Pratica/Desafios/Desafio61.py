""" Refaça o Desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão,
usando a estrutura while"""
pri = int(input('Digite aqui o primeiro termo da sua PA: '))
ra = int(input('Digite aqui a razão da sua PA: '))
pa = pri + (10 * ra)
termo = pri
print(f'Estes são os primeiros 10 termos da sua PROGRESSÃO ARITIMÉTICA: ')
print(pri)
while termo != pa:
    termo += ra
    print(termo)

# CORREÇÃO
print('Gerador de PA')
print('-=-' * 20)
prim = int(input('Primeiro termo: '))
raz = int(input('Razão da PA'))
termo = prim
cont = 1
while cont <= 10:
    print(termo, ' >> ', end='')
    termo += raz
    cont += 1
print('Fim')
