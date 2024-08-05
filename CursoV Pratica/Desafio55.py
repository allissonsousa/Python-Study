"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos"""

for i in range(1, 5+1):
    peso = int(input(f'Peso {i}: '))
    pesos = peso
    if pesos >= peso:
        print(pesos)