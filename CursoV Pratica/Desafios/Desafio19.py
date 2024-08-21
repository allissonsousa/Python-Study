""" Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo os nomes deles e escrevendo o nome escolhido"""

from random import choice
n1 = input('Nome do primero aluno:')
n2 = input('Nome do segundo aluno:')
n3 = input('Nome do terceiro aluno:')
n4 = input('Nome do quarto aluno:')
lista = [n1, n2, n3, n4]
sort = choice(lista)        # choice sorteia um elemento da lista
print(f'O aluno sorteado para apagar o quadro desta vez é o(a) {sort}')

# Outra forma de ser feito
# from random import choice
nm1 = str(input('Primeiro aluno:'))
nm2 = str(input('Segundo aluno:'))
nm3 = str(input('Terceiro aluno:'))
nm4 = str(input('Quarto aluno'))
les = [nm1, nm2, nm3, nm4]
escolhido = choice(les)
print(f'O aluno escolhido foi {escolhido}')


