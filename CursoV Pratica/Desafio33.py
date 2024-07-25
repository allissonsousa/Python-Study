"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor"""
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terçeiro número: '))
if (n1 > n2) and (n1 > n3):
    print('O primeiro número é o maior')
elif (n2 > n1) and (n2 > n3):
    print('O segundo número é o maior')
elif (n3 > n1) and (n3 > n2):
    print('O terceiro número é o maior')
else:
    print('Os números são iguais')

if (n1 < n2) and (n1 < n3):
    print('O primeiro número é o menor')
elif (n2 < n1) and (n2 < n3):
    print('O segundo número é o menor')
elif (n3 < n1) and (n3 < n2):
    print('O terceiro número é o menor')
else:
    print('Os números são iguais')1