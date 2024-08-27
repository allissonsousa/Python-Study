"""Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços, organizando os dados em forma tabular"""
tulipa = ('Banana', 4, 'Picanha', 89, 'Café', 56, 'Refri', 8, 'Bolo', 17, 'Macarrão', 6)
produto = ''
preco = 0

print('TABELA DE PREÇOS'.center(50, '='))
for i in range(0, len(tulipa), 2):
    produto = tulipa[i]
    preco = tulipa[i + 1]
    larg = 40 - (len(produto) + len(str(preco)))
    print(produto, end=' ')
    print('-'.center(larg, '-'), end=' ')
    print(f'R${preco:.2f}')

print('=' * 50)