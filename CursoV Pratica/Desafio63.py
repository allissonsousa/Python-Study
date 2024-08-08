"""Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma sequencia fibonacci"""
n = int(input('Quantos termos da SEQUENCIA FIBONACCI você deseja ver ? '))
seq = 0
a = 0
b = 0
c = 0
while seq != n:
    a += 1
    print(a)
