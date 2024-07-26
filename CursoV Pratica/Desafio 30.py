"""Crie um programa que leia um número interio e mostre na tela se ele é Par ou Impar"""

n = int(input('Digite aqui um número:'))
if n % 2 == 0:
    print('Este número é par!')
else:
    print('Este número é impar!')

# CORREÇÃO
num = int(input('Me diga um número qualquer: '))
res = num % 2
if res == 0:
    print(f'O número {num} é PAR!')
else:
    print(f'O número {num} é IMPAR!')