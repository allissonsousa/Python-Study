"""Crie um programa que tenha uma tupla com varias palavras ( nao usar acentos) Depois disso, voce deve mostrar, para
cada palavra, quais são as suas vogais"""
tulipa = ('Panda', 'Mercado', 'Pedra', 'Comercial', 'Mexirica', 'Corda', 'Motocross', 'Roupas')
for i in range(0, len(tulipa)):
    palavra = str(tulipa[i])
    print(palavra)
    for c in range(0, len(palavra)):
        if palavra[c] in 'AaEeIiOoUu':
            print(palavra[c])
