# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input('Digite aqui o preço do produto:'))
np = p - (p * 5 / 100)
print(f'O preço deste produto com desconto será: R${np:.2f}')
