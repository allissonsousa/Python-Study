# Desenvolva um programa que leia as duas notas de um aluno, e calcule e mostre a sua média

# COMO EU FIZ
nota1 = float(input('Digite aqui a primeira nota:'))
nota2 = float(input('Digite aqui a segunda nota:'))
med = (nota1 + nota2) / 2

print(f'A sua média de pontos é: {med:.2f}')

# OUTRA FORMA DE SER FEITO
n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
m = (n1 + n2) / 2
print(f'A média entre {n1} e {n2} é {m:.2f}!')
