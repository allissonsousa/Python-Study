"""Faça um programa que leia um número inteiro e diga se ele é ou nao número primo"""
n = int(input('Digite aqui um número: '))
if n == 2 or n == 3 or n == 5:
    print('Primo')
elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
    for i in range(2, n+1):
        if n % i == 0:
            print(f'Este número é divisivel por 1 e {i}')
else:
    print('Não primo')

# CORREÇÃO
num = int(input('Digite um número: '))
tot = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[35m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print(i, end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
