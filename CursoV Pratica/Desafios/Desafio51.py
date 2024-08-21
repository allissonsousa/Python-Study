"""Desenvolva um programa que leia o primeiro termo e a razão de  uma progressão aritimetica.
No final mostre os 10 primeiros termos dessa progressão"""
p = int(input('Digite aqui o primeiro termo da sua progreção aritimética: '))
r = int(input('Digite aqui a razão da sua progreção aritimética: '))
gap = r * 10 + p
for i in range(p, gap, r):
    print(i)

# CORREÇÃO
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = pri + (10-1) * raz
for i in range(pri, dec+raz, raz):
    print(i, end=' --> ')
print('Fim')