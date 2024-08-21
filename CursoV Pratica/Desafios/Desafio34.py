"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para salários inferiores ou igual, o aumento é de 15%."""
sal = float(input('Qual o seu salario ? : '))
if sal >= 1250:
    print(f'O novo valor do seu salario com 10% de aumento será R${sal + (sal * 10 / 100):.2f}')
elif sal <= 1250:
    print(f'O novo valor do seu salário com 15% de aumento será R${sal + (sal * 15 / 100):.2f}')

# CORREÇÃO
s = float(input('Qual o salario ?'))
if s <= 1250:
    n = s + (s * 15 / 100)
else:
    n = s + (s * 10 / 100)
print(f'Quem ganhava R${s:.2f} passa a ganhar R${n:.2f}')