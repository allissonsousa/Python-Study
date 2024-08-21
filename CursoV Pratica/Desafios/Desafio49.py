"""Refaça o exercício 09, mostrando o número qe ousuário escolher, só que agora utilizando laço for"""
n = int(input('Digite aqui um número para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
