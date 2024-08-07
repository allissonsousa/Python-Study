"""Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso"""

op = 0
while op != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    op = int(input('''Oque você deseja fazer com esses valores?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa\n'''))
    if op == 1:
        res = n1 + n2
        print('Soma =', res)
    elif op == 2:
        res = n1 * n2
        print('Multiplicação =', res)
    elif op == 3:
        if n1 > n2:
            res = n1
            print('Maior =', res)
        else:
            res = n2
            print('Maior =', res)
print('Fim do programa!!!')