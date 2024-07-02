# Voltando aos estudos de pyhton do zero, pra nada

# 1---

nome = input('Qual seu nome?')
idade = input('Quantos anos você tem ?')
peso = input('Quanto você pesa ?')
print(nome, peso, idade)  # USO DE VÍRGULA PARA MELHOR CONTATENAÇÃO ENTRE AS VARIÁVEIS, SENDO ELAS STR E NUMB

# Desafio 1---
# script python com nome de uma pessoa e retorna uma mensagem de boas vindas com o nome

nome = input('Qual seu nome?')
print('Seja muito bem vindo(a)', nome)  # NÃO ESQUECER DA BOA E VELHA VÍRGULA

# Desafio 2---
# script python q leia o dia, mês e o ano de nsacimento de uma pessoa e mostre a mensagem com a data formatada

dia = input('Seu dia de nascimento:')
mes = input('Seu mês de nascimento:')
ano = input('Seu ano de nascimento:')
print('Você nasceu no dia', dia, 'de', mes, 'do ano de', ano)

# Desafio 3---
# script python que leia dois números e tente mostras a soma entre eles

num1 = input('Digite o primeiro número da soma:')
num2 = input('Digite o segundo número da soma:')
soma = int(num1) + int(num2)  # USO DO INT PRA FAZER A STR DO NÚMERO SE TORNAR UM VALOR INT S0MÁVEL
print('A soma destes números é:', soma)

num1 = input('Digite o primeiro número da soma:')
num2 = input('Digite o segundo número da soma:')
soma = int(num1) + int(num2)
print(f'A soma entre {num1} e {num2} é igual a {soma}')

# Operações aritiméticos
# operadores   + adição, - subtração, *multiplicação, / divisão, ** potência, // divisão inteira, % resto da divisão

'''
5 + 2 == 6
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 ==25
5 // 2 ==2 RESTA 1 DA DIVISÃO, na divisão inteira não tem resto, e o resultado nunca é float

5 % 2 == 1   O RESTO VEM PRA CA'''

# Ordem de precedência: 1-(), 2-**, 3- * / % //, 4_ + -


nome = input('Qual seu nome?')
print(f'Prazer em te conhecer`{nome:^20}!')  # :20 é o a quantidade de espaço q a palavra nome ira ocupar, e
# ^ é o alinhamento justificado, < e > é dos lados direito e esquerdo


# Mais funcionalidades

n1 = int(input('Digite um valor?'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s} e a \n divisão é {m:.3f}', end='')  # \n é a quebra de linha de um print, e end= é pra conectar os
print(f'Divisão inteira {di} e potência {e}')  # os dois prints


