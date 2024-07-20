"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
ex >> 3210
unidades 0
dezenas 1
centenas 2
milhares 3"""
nume = str(input('Digite um numero de 0 a 9999:'))
todos = list(nume)
print(todos[0])
"""" PARTIR UM NUMERO EM 4 PARTES MESMO QUE VAZIAS"""