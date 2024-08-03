"""Faça um programa que calcule a soma entre todos os números impares que são multiplos de três
e que se encontram no intervalo de 1 até 500"""
s = 0
for i in range(0, 500):
    if i % 2 == 1 and i % 3 == 0:
        s += i
        print(s)
print(s)