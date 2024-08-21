"""Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas não atingiram a maioridade e quantas ja são de maior
considere a maioridade 21 anos"""
from datetime import date
t = date.today().year
quant = 0
for i in range(1, 8):
    pessoa = int(input('Em que ano você nasceu?'))
    idade = t - pessoa
    if idade >= 21:
        quant += 1
if quant == 0:
    print('Nenhuma dessas pessoas é maior de idade')
else:
    print(f'{quant} Pessoas dessas são maiores de idade e {7-quant} ainda não são de maior')

# CORREÇÃO
# import date
atual = date.today().year
totma = 0
totme = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}° pessoa nasceu? '))
    ida = atual - nasc
    if ida >= 21:
        totma += 1
    else:
        totme += 1
print(f'Ao todo tivemos {totma} pessoas de maior, e {totme} pessoas de menor')
