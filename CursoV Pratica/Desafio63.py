"""Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma sequencia fibonacci"""
n = int(input('Quantos termos da SEQUENCIA FIBONACCI você deseja ver ? '))
cont = 0   # serve só de contador pro laço
n1 = 1
n2 = 0
ac = 0
print(f'Os {n} primeiros termos da SEQUÊNCIA FIBONACCI são:')
while n != cont:
    cont += 1
    ac = n1 + n2
    if ac > 0:
        n1 = n2
        n2 = ac
    print(ac)


