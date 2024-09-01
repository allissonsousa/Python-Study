"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
a = quantas vezes aparecer o valor 9
b = em que posição foi digitado o primeiro valor 3
c = quais foram os números pares"""
tulipa = []
pares = 0
for i in range(0, 4):
    n = int(input('Digite um valor: '))
    tulipa.append(n)
    if n % 2 == 0:
        pares += 1


print(f'''Sua tupla é: {tuple(tulipa)}
O número 9 apareceu {tulipa.count(9)} vezes
A sua tupla contém {pares} números pares''')
if 3 in tulipa:
    print(f'O número 3 apareceu pela primeira vez na posição {tulipa.index(3) + 1}')


# CORREÇÃO
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram:', end=' ')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')
