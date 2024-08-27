"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão  na tupla"""
from random import randint

tulipa = []
maior = 0
menor = 0
for i in range(0, 5):
    n = randint(0, 10)
    tulipa.append(n)

for i in range(0, len(tulipa)):
    if tulipa[i] > maior:
        maior = tulipa[i]
    if i == 0:
        menor = tulipa[i]
    elif tulipa[i] < menor:
        menor = tulipa[i]
print(f'A tupla gerada aleatoriamente é : {tuple(tulipa)}')
print(f'O maior valor desta tupla é o número {maior}')
print(f'O menor valor desta tupla é o  número {menor}')
