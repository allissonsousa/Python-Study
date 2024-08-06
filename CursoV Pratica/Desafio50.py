"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares,
Se o valor digitado for impar, desconsidere-0"""
s = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i}° número: '))
    if n % 2 == 0:
        s += n
print(s)

# CORREÇÃO
soma = 0
cont = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}° valor:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma destes é {soma}')
