"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número ja exista la dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados
em ordem crescente"""
ls = []
quer = 'S'
while quer == 'S':
    n = int(input('Digite um valor: '))
    if n not in ls:
        print('Valor adicionado com sucesso')
        ls.append(n)
    else:
        print('Valor repetido. Não será adicionado a lista..')
    quer = str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]

print(f'\nVocê digitou os valores {sorted(ls)}')

# CORREÇÃO

numeros = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado a lista com sucesso!')
    else:
        print('Valor duplicado não aceito! ')
    r = str(input('Quer continuar ? [s/n] ')).strip().upper()[0]
    if r in 'N':
        break

print('-=-' * 30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')