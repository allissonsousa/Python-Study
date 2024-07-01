# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
import math

num = int(input('Digite um número:'))
numx2 = num * 2
numx3 = num * 3
numxx2 = math.sqrt(num)

print(f'O dobro deste número é: {numx2} \nO triplo desse número é: {numx3} \nA raiz quadrada desse número é: {numxx2}')