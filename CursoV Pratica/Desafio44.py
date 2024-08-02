"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento?
- a vista dinheiro ou cheque: 10% de desconto
- a vista no cartao: 5% de desconto
- em ate 2x no cartao: preço normal
- 3x ou mais no cartao: 20% de juros"""
preco = float(input('Qual o valor do produto que você está comprando ? R$'))
pagamento = int(input('Digite o número de acordo com a sua forma de pagamento: \n'  # devia ter usado o '''
                      '1 = A vista no dinheiro\n'
                      '2 = A vista no cartão\n'
                      '3 = Em até 2x no cartão\n'
                      '4 = 3x ou mais no cartão\n'))
valor = ''
if pagamento == 1:
    valor = preco - (preco * 10 / 100)
elif pagamento == 2:
    valor = preco - (preco * 5 / 100)
elif pagamento == 3:
    valor = preco
elif pagamento == 4:
    valor = preco + (preco * 10 / 100)
print(f'O valor a ser pago pelo produto sera de R${valor:.2f}')

# CORREÇÃO
if pagamento == 1:
    valor = preco - (preco * 10 / 100)
elif pagamento == 2:
    valor = preco - (preco * 5 / 100)
elif pagamento == 3:
    valor = preco
    parcela = preco / 2
    print(f'Sua compra será parcelada em 2 vezes de R${parcela:.2f}')
elif pagamento == 4:
    valor = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas ?'))
    parcela = valor / totparc
    print(f'A sua compra sera parcelada em {totparc} vezes de R${parcela:.2f}')
else:
    valor = 0
    print('\033[1:31mOPÇÃO INVALIDA DE PAGAMENTO, TENTE NOVAMENTE!!\033[m')

print(f'O valor a ser pago pelo produto sera de R${valor:.2f}')
