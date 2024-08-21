"""Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos ANOS ele vai pagar.
 Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
 """
casa = float(input('Qual o valor da casa que voce deseja adiquirir ? R$'))
sal = float(input('Qual o valor do seu salário mensal ? R$'))
ano = int(input('Em quantas Anos você planeja pagar seu empréstimo ? '))
prest = ano * 12  # cada ano tem 12 meses, logo 12 parcelas
mens = float(casa / prest)
if mens > (sal * 30 / 100):  # calcula se a parcela é maior que 30% do salário
    print(f'Infelizmente o seu salário não é compativel com o valor da parcela de R${mens:.2f}, empréstimo NEGADO')
else:
    print(f'Parabéns o seu empréstimo foi APROVADO, você deverá pagar {prest} parcelas mensais de R${mens:.2f}')
print('Obrigado por nos consultar, tenha um bom dia!')

