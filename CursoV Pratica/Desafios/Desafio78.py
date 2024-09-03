"""Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual é o maior e o menor
valor digitado e as suas respectivas posições na lista"""
ls = []
for i in range(5):
    n = int(input('Digite um valor: '))
    ls.append(n)
ls.sort()
print(ls)