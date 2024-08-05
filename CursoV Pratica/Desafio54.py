"""Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas não atingiram a maioridade e quantas ja são de maior
considere a maioridade 21 anos"""
from datetime import date
t = date.today().year
quant = 0
for i in range(1, 7+1):
    pessoa = int(input('Em que ano você nasceu?'))
    idade = t - pessoa
    if idade >= 21:
        quant += 1
if quant == 0:
    print('Nenhuma dessas pessoas é maior de idade')
else:
    print(f'{quant} Pessoas dessas são maiores de idade e {7-quant} ainda não são de maior')