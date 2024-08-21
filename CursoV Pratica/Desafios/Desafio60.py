""" Faça um programa que leia um número qualquer e mostre o seu fatorial
ex :
5! = 5 x 4 x 3 x 2 x 1 = 120
Faça com WHILE e também faça com o uso do FOR"""
from math import factorial

n = int(input('Digite um número e descubra o seu fatorial:\n'))
val = n
ac = 0
va = n
while n != 1:
    n -= 1
    print()
    va = n * va
    if va > ac:
        ac = va

print(f'O fatorial de {val} é {ac}!')

# CORREÇÃO 1
num = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print(f'O fatorial de {num} é {f}')

# CORREÇÃO 2
nume = int(input('Digite aqui um número para calcular o seu fatorial : '))
c = nume
f = 1   # Acumulador de vezes igual *=  sempre começa com o valor 1, por isso n deu certo outras vezes q tentei, n sabia
print(f'Calculando {nume}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)