"""Crie um programa que leia varios números integrados pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de pararda. No final, mostre quantos números foram digitados e qual foi a
soma entre eles ( desconsiderando o flag 999)"""
n = 0
ac = 0
cont = 0
while n != 999:
    n = int(input('Digite aqui um número : '))
    cont += 1
    if n != 999:
        ac += n
print(f'Voce digitou {cont} números e a soma entre eles é = {ac}')

