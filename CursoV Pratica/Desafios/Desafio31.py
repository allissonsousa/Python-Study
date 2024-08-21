"""Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas"""

d = int(input('Digite aqui a distância da sua viagem em kilometros: '))
if d <= 200:
    print(f'Sua passagem custará R${d * 0.50:.2f} !')
else:
    print(f'Sua passagem custará R${d * 0.45:.2f} !')

# CORREÇÃO
dist = float(input('Qual é a distância da sua viagem ?'))
print(f'Você está prestes a começar uma viagem de {dist}km')
if dist <= 200:
    pre = dist * 0.50
else:
    pre = dist * 0.45
print(f'E o preço da sua passagem será de R${pre:.2f}')
