"""Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado
No final mostre a matriz na tela, com a formataçao correta"""
from os.path import split
x = ''
matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        valor = [int(input(f'Digite um valor para [{l},{c}]: '))]
        matriz[l].append(valor)

print('-=-' * 12)

for m in range(0,3):
    for h in range(0,3):
        if h != 2:
            x = ' '
        else:
            x = '\n'
        print(matriz[m][h],end = x)


#---------------------------------------
# CORREÇÃO

mat = [[0,0,0],[0,0,0],[0,0,0]]
for li in range(0,3):
    for cas in range(0,3):
        mat[li][cas] = int(input(f'Digite um valor para [{li}], [{cas}]: '))

print('-=-' * 30)
for li in range(0,3):
    for cas in range(0,3):
        print(f'[{mat[li][cas]:^5}',end=' ')
    print()



