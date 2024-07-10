""" O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada"""

from random import shuffle
n1 = input('Primeiro Aluno :')
n2 = input('Segundo Aluno :')
n3 = input('Terceiro Aluno :')
n4 = input('Qaurto Aluno :')
ls = [n1, n2, n3, n4]
shuffle(ls)
print(f'Os alunos devem se apresentar na respectiva ordem: {ls}')
