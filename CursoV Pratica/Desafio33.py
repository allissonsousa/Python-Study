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
    print('Os números têm o mesmo valor')

if (n1 < n2) and (n1 < n3):
    print('O primeiro número é o menor')
elif (n2 < n1) and (n2 < n3):
    print('O segundo número é o menor')
elif (n3 < n1) and (n3 < n2):
    print('O terceiro número é o menor')
else:
    print('Os números têm o mesmo valor')
# Esse exercicio ficou uma bagunça, com certeza tem uma forma mais eficiente


# CORREÇÃO
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# colocando o a como menor, pra diminuir um if
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')