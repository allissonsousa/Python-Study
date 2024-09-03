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

print(f'\nVocê digitou os valores {ls}')