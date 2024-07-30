"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de coversão:
-1 para binário
-2 para octal
-3 para hexadecimal
"""

num = int(input('Digite um número: '))
base = str(input('Qual base de conversão voce vai usar pra transformar esse número? '.upper()))
if base == 'BINÁRIO':
    conv = 1
elif base == 'OCTAL':
    conv = 2
elif base == 'HEXADECIMAL':
    conv = 3

