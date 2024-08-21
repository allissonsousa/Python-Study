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

# CORREÇÃO
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa
    ''')
    opc = int(input('Qual a sua opção? '))
    if opc == 1:
        soma = num1 + num2
        print(f'A soma entre  {num1} e {num2} é {soma}')
    elif opc == 2:
        prod = num1 * num2
        print(f'A multiplicação entre {num1} e  {num2} é {prod}')
    elif opc == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior valor entre {num1} e {num2} é {maior}')
    elif opc == 4:
        print('Informe os números novamente!')
        num1 = int(input('´Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente')
    print('=-=' * 23)
opc = int(input('Qual a sua opção?'))
