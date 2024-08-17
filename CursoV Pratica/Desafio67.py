"""Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuário
O programa sera interrompido quando o  número solicitado foi negativo"""
n = 1
while n >= 1:
    print('-' * 40)
    n = int(input('Você quer ver a tabuada de qual número? '))
    print('-' * 40)
    if n != 0:
        for i in range(1, 11):
            print(f'{n} x {i} = {n * i}')
            i += 1

print('Você digitou um valor não válido. PROGRAMA ENCERRADO!!')


