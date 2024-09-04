"""Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual é o maior e o menor
valor digitado e as suas respectivas posições na lista"""
"""ls = []
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
        print(f'{evo}...', end='')"""


# CORREÇÃO
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digte um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-=' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {men} mas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')