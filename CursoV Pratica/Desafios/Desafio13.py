# Faça um algoritmo que leia o salário de  um funcionário e mostre seu novo salário, com 15% de aumento

sal = float(input('Digite aqui o valor do seu salário:'))
ns = sal + (sal * 15 / 100)
print(f'Seu novo salário com aumento de 15% é R${ns:.2f}')
