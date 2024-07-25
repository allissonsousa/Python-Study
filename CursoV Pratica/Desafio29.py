"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80kmh, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite"""

v = int(input('Digite aqui a velocidade registrada do veículo:  '))
if v > 80:
    print(f'Este veículo ultrapassou o limite de velocidade e deverá receber uma multa de R${(v - 80) * 7},00')
else:
    print('Este veículo esta trafegando em velocidade condizente com os limites da via!')