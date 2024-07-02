# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

# FORMA COMO FIZ
num = int(input('Digite um número inteiro:'))
n0 = num * 0
n1 = num * 1
n2 = num * 2
n3 = num * 3
n4 = num * 4
n5 = num * 5
n6 = num * 6
n7 = num * 7
n8 = num * 8
n9 = num * 9
n10 = num * 10

print(f'TABUADA:\n'
      f'0 X {num} = {n0}\n'
      f'1 X {num} = {n1}\n'
      f'2 X {num} = {n2}\n'
      f'3 X {num} = {n3}\n'
      f'4 X {num} = {n4}\n'
      f'5 X {num} = {n5}\n'
      f'6 X {num} = {n6}\n'
      f'7 X {num} = {n7}\n'
      f'8 X {num} = {n8}\n'
      f'9 X {num} = {n9}\n'
      f'10 X {num} = {n10}\n')

# COMO PODE SER FEITO USANDO  MENOS MEMÓRIA
n = int(input('Digite um número para ver sua tabuada:'))
print('_' * 12)
print(f'Tabuada\n'
      f'{n} x 1 = {n * 1}\n'
      f'{n} x 2 = {n * 2}\n'
      f'{n} x 3 = {n * 3}\n'
      f'{n} x 4 = {n * 4}\n'
      f'{n} x 5 = {n * 5}\n'
      f'{n} x 6 = {n * 6}\n'
      f'{n} x 7 = {n * 7}\n'
      f'{n} x 8 = {n * 8}\n'
      f'{n} x 9 = {n * 9}\n'
      f'{n} x 10 = {n * 10}\n')
print('_' * 12)
