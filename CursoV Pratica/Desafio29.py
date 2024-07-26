"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80kmh, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite"""

v = int(input('Digite aqui a velocidade registrada do veículo:  '))
if v > 80:
    print(f'Este veículo ultrapassou o limite de velocidade e deverá receber uma multa de R${(v - 80) * 7},00')
else:
    print('Este veículo esta trafegando em velocidade condizente com os limites da via!')

# CORREÇÃO
vel = float(input('Qual é a velocidade atual do carro ?'))
if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade de 80 km/h')
    multa = (vel - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')
