"""Desenvolva um programa que leia o comprimênto de três retas e diga ao usuário se ela podem ou não
formar um triângulo"""
print('Vamos ver se você consegue formar um triângulo, digite a baixo a medidas dos lados do seu triângulo')
l1 = float(input('Primeiro lado:'))
l2 = float(input('Segundo lado:'))
l3 = float(input('Terceiro lado:'))
# A soma de dois lados sempre tem q ser maior que o terceiro lado
if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l1:
    print('Parabéns, com essas medidas você pode construir um triângulo !!')
else:
    print('Com essas medidas não é possivel construir um triângulo !!')

# CORREÇÃO
# praticamente igual ao código q eu fiz
