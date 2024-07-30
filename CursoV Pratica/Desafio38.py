"""Escreva um programa que leia dois numeros inteiros e comprare-os, mostrando na tela uma mensagem :
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais')