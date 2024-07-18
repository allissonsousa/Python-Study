"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
ex >> 3210
unidades 0
dezenas 1
centenas 2
milhares 3"""
num = str(input('Digite um numero de 0 a 9999:'))
num.zfill(3)
print(f'Milhar: {num[0:1]}')
print(f'Centenas: {num[1:2]}')
print(f'Dezenas: {num[2:3]}')
print(f'Unidades: {num[3:]}')
"""" PARTIR UM NUMERO EM 4 PARTES MESMO QUE VAZIAS"""