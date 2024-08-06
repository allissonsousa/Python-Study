"""Faça um programa que calcule a soma entre todos os números impares que são multiplos de três
e que se encontram no intervalo de 1 até 500"""
s = 0
for i in range(0, 501):
    if i % 2 == 1 and i % 3 == 0:
        s += i
        print(s)
print(s)

# CORREÇÃO
soma = 0    # acumulador
cont = 0    # contador
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        soma += i
print(f'A soma de todos os {cont} valores solicitados é {soma}')

