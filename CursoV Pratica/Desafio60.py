""" Faça um programa que leia um número qualquer e mostre o seu fatorial
ex :
5! = 5 x 4 x 3 x 2 x 1 = 120
Faça com WHILE e também faça com o uso do FOR"""

n = int(input('Digite um número e descubra o seu fatorial:\n'))
val = n
ac = 0
va = n
while n != 0:
    n -= 1
    va = n * va
    if va > ac:
        ac = va

print(f'O fatorial de {val} é {ac}!')