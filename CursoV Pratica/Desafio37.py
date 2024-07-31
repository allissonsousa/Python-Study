"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de coversão:
-1 para binário
-2 para octal
-3 para hexadecimal
"""

num = int(input('Digite um número: '))
base = int(input('Qual base de conversão voce vai usar pra transformar esse número?\n'
                 '1 = Binário\n'
                 '2 = Octal\n'
                 '3 = Hexadecimal\n'))
conv = ''
lin = ''
if base == 1:
    conv = (bin(num)[2:])  # o 2: é para formatar a exibiçao que sempre começa com 0b, ou 0o, ou 0h
    lin = 'Binário'
elif base == 2:
    conv = (oct(num)[2:])
    lin = 'Octal'
elif base == 3:
    conv = (hex(num)[2:])
    lin = 'Hexadecimal'
print(f'Este número convertido para {lin} será = {conv}')