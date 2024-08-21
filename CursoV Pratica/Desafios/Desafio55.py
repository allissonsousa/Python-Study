"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos"""
menor = 0
maior = 0
for i in range(1, 6):
    peso = float(input(f'Peso da {i}° pessoa: '))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < peso:
            menor = peso
print(f'O maior peso lido foi de {maior}KG e o menor foi de {menor}KG')
