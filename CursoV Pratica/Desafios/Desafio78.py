"""Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual é o maior e o menor
valor digitado e as suas respectivas posições na lista"""
ls = []
maior = 0
menor = 0
for i in range(5):
    n = int(input('Digite um valor: '))
    ls.append(n)
for el in range(0, len(ls)):
    if el == 0:
        menor = ls[el]
    elif ls[el] < menor:
        menor = ls[el]
    if ls[el] > maior:
        maior = ls[el]

print(f'Você digitou os valores {ls}')
print(f'O maior valor digitado foi {maior}  nas posições: ', end='')
for val in range(0, len(ls)):
    if ls[val] == maior:
        print(f'{val}...', end='')

print(f'\nO menor valor digitado foi {menor}  nas posições: ', end='')
for evo in range(0, len(ls)):
    if ls[evo] == menor:
        print(f'{evo}...', end='')