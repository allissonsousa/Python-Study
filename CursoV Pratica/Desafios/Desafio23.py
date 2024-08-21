"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
ex >> 3210
unidades 0
dezenas 1
centenas 2
milhares 3"""
num = int(input('Digite um numero de 0 a 9999:'))
u = num // 1 % 10       # Divisão inteira do número, e pega o valor do resto
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}\n'
      f'Unidades: {u}\n'
      f'Dezenas: {d}\n'
      f'Centenas: {c}\n'
      f'Milhar: {m}')

# Ralei muito nesse desafio, nao consegui usando os metodos q aprendi
# Na resoluçao o professor so usou calculos matematicos pra conseguir obter o valor de cada casa
"""" PARTIR UM NUMERO EM 4 PARTES MESMO QUE VAZIAS"""