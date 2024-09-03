"""Crie um programa que tenha uma tupla com varias palavras ( nao usar acentos) Depois disso, voce deve mostrar, para
cada palavra, quais são as suas vogais"""
tulipa = ('Panda', 'Mercado', 'Pedra', 'Comercial', 'Mexirica', 'Corda', 'Motocross', 'Roupas')
for i in range(0, len(tulipa)):
    palavra = str(tulipa[i])
    print(f'\nNa palavra {palavra} podemos encontrar as vogais:', end=' ')
    for c in range(0, len(palavra)):
        if palavra[c] in 'AaEeIiOoUu':
            print(palavra[c], end=' ')


# CORREÇÃO
palavras = ('Panda', 'Mercado', 'Pedra', 'Comercial', 'Mexirica', 'Corda', 'Motocross', 'Roupas')
for p in palavras:
    print(f'\nNa palavra {p}, temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
