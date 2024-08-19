"""Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuário qual será o valor
a ser sacado (int) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs=  considere que o caixa possui notas de 50, 20, 10 e 1 real"""
# SÓ EU E O DIABO SABEM OQUE ACONTECEU QUANDO EU FIZ ESSE CODIGO PORQUEIRA
print('=' * 60)
print('CAIXA ELETRONICO'.center(60, ' '))
print('=' * 60)
valor = int(input('Qual o valor que deseja sacar? R$'))
cinquenta = 0
vinte = 0
dez = 0
um = 0
if valor >= 50:
    cinquenta = valor // 50
    resto = valor % 50
    if resto < 50:
        vinte = resto // 20
        resto = resto % 20
        if resto < 20:
            dez = resto // 10
            resto = resto % 10
            if resto < 10:
                um = resto
elif valor >= 20:
    vinte = valor // 20
    resto = valor % 20
    if resto < 20:
        dez = resto // 10
        resto = resto % 10
        if resto < 10:
            um = resto
elif valor >= 10:
    dez = valor // 10
    resto = valor % 10
    if resto < 10:
        um = resto
else:
    um = valor

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