""" Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo os nomes deles e escrevendo o nome escolhido"""
import random

n1 = input('Nome do primero aluno:')
n2 = input('Nome do segundo aluno:')
n3 = input('Nome do terceiro aluno:')
n4 = input('Nome do quarto aluno:')
lista = [n1, n2, n3, n4]
sort = random.choice(lista)
print(f'O aluno sorteado para apagar o quadro desta vez é o(a) {sort}')
