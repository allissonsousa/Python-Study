"""Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuário vai continuar
no final, mostre :
A = qual é o total de gasto na compra
B = quantos produtos custam mais de R$ 1000
C = qual é o nome do produto mais barato"""

print('-' * 60)
print('LOJA DO ALINHO'.center(60, '.'))
print('-' * 60)
total = 0
caro = 0
baratonome = ''
baratovalor = 99999999999999999999999999999
continua = ''
while continua != 'N':
    produto = str(input('Nme do produto: ')).strip().upper()
    preco = float(input('Preço do produto: R$'))
    continua = str(input('Deseja continuar comprando? [S/N] ')).strip().upper()
    total += preco
    if preco >= 1000:
        caro += 1
    if preco < baratovalor:
        baratovalor = preco
        baratonome = produto

print('Fim do programa'.center(60, '-'))
print(f'''O total da compra foi de R${total:.2f}
Voce comprou {caro} produtos que custam mais que R$1000,00
O produto mais barato foi a {baratonome} custando {baratovalor}''')

# CORREÇÃO
tot = totmil = meno = cont = 0
bar = ''

while True:
    prod = str(input('Nome do Produto: '))
    prc = float(input('Preço: R$'))
    tot += prc
    cont += 1
    if prc > 1000:
        totmil += 1
    if cont == 1 or prc < meno:
        meno = prc
        bar = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do programa'))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {totmil} produtos custando mai de R$1000,00')
print(f'O produto mais barato foi o {bar} que custa R${meno:.2f}')

