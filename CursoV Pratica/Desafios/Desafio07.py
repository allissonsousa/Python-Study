# Desenvolva um programa que leia as duas notas de um aluno, e calcule e mostre a sua média

# COMO EU FIZ
nota1 = float(input('Digite aqui a \033[33mprimeira nota\033[m: '))
nota2 = float(input('Digite aqui a \033[35msegunda nota\033[m: '))
med = (nota1 + nota2) / 2

print(f'A sua \033[36mmédia\033[m de pontos é: \033[34m{med:.2f}\033[m')

# OUTRA FORMA DE SER FEITO
n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
m = (n1 + n2) / 2
print(f'A média entre {n1} e {n2} é {m:.2f}!')
