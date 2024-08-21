"""Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuário
O programa sera interrompido quando o  número solicitado foi negativo"""
n = 1
while n >= 1:
    print('-' * 40)
    n = int(input('Você quer ver a tabuada de qual número? '))
    if n < 0:
        break
    print('-' * 40)
    if n != 0:
        for i in range(1, 11):
            print(f'{n} x {i} = {n * i}')
            i += 1

print('Você digitou um valor não válido. PROGRAMA ENCERRADO!!')

# CORREÇÃO
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 30)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('=' * 30)
