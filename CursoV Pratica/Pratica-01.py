#Voltando aos estudos de pyhton do zero, pra nada

#1---

nome = input('Qual seu nome?')
idade = input('Quantos anos você tem ?')
peso = input('Quanto você pesa ?')
print (nome, peso, idade)   #USO DE VÍRGULA PARA MELHOR CONTATENAÇÃO ENTRE AS VARIÁVEIS, SENDO ELAS STR E NUMB



#Desafio 1---
#script python com nome de uma pessoa e retorna uma mensagem de boas vindas com o nome

nome = input('Qual seu nome?')
print('Seja muito bem vindo(a)',nome)    #NÃO ESQUECER DA BOA E VELHA VÍRGULA

#Desafio 2---
#script python q leia o dia, mês e o ano de nsacimento de uma pessoa e mostre a mensagem com a data formatada

dia = input('Seu dia de nascimento:')
mes = input('Seu mês de nascimento:')
ano = input('Seu ano de nascimento:')
print ('Você nasceu no dia', dia ,'de', mes ,'do ano de', ano)

#Desafio 3---
#script python que leia dois números e tente mostras a soma entre eles

num1 =  input('Digite o primeiro número da soma:')
num2 =  input('Digite o segundo número da soma:')
soma =  int(num1) + int(num2)                       #USO DO INT PRA FAZER A STR DO NÚMERO SE TORNAR UM VALOR INT S0MÁVEL
print('A soma destes números é:',soma)

