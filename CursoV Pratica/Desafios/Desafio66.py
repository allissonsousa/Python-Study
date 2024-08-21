"""Crie um programa que leia varios números inteiros. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(sem a flag)"""
n = 0
acumulador = 0
soma = 0
while n != 999:
    n = int(input('Digite aqui um valor [999 para parar]: '))
    if n != 999:
        acumulador += 1
        soma += n
print(f'Voce digitou {acumulador} valores, que juntos somam {soma}')

# CORREÇÃO
some = 0
cont = 0
while True:
    num = int(input('Digite um valor: [999 para parar] '))
    if num == 999:
        break
    cont += 1
    some += num
print(f'A soma dos {cont} valores foi {some}')