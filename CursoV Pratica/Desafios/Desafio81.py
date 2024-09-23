"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A= quantos números foram digitados
B= A lista de valores, ordenada de forma decrescente
C= Se o valor 5 foi digitador e está ou não na lista"""

el = 0
ls = []
cont = 'S'
while cont == 'S':
    n = int(input('Digite um valor: '))
    ls.append(n)
    el += 1
    cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]

ls.sort(reverse=True)
print('+=' * 30)
print(f'Você digitou {el} elementos')
print(f'Os valores em ordem decescente são {ls}')
if 5 in ls:
    print('O valor 5 faz parte da sua lista!')
else:
    print('O valor 5 não faz parte da sua lista!')
