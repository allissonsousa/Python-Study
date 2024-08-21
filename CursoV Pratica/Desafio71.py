"""Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuário qual será o valor
a ser sacado (int) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs=  considere que o caixa possui notas de 50, 20, 10 e 1 real"""
# SÓ EU E O DIABO SABEM OQUE ACONTECEU QUANDO EU FIZ ESSE CODIGO PORQUEIRA
print('=' * 60)
print('CAIXA ELETRONICO'.center(60, ' '))
print('=' * 60)
valor = int(input('Qual o valor que deseja sacar? R$'))
nota = valor
i = 0
cinquenta = um = vinte = dez = 0    # armazenam a quantidades de notas pra imprimir na tela posteriormente
valores = [50, 20, 10, 1]      # notas disponiveis pra sacar
while valor != 0:       # valor vai ser o resto das divisões que serão feitas
    for i in valores:   # para nota na lista
        if valor >= i:      # se a o valor for maior ou igual a nota, divide o valor por i e o resto da divisão passa a
            nota = valor // i                                                   # a ser o novo valor
            valor = valor % i
            break

    if i == 50:
        cinquenta += nota
    if i == 20:
        vinte += nota
    if i == 10:
        dez += nota
    if i == 1:
        um += nota


if cinquenta != 0:
    print(f'Total de {cinquenta} cédulas de cinquenta')
if vinte != 0:
    print(f'Total de {vinte } cédulas de vinte')
if dez != 0:
    print(f'Total de {dez} cédulas de dez')
if um != 0:
    print(f'Total de {um} cédulas de um')
print('==' * 30)
print('Volte sempre ao banco do Alinho'.center(60, ' '))


