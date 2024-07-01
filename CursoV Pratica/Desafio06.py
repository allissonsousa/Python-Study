# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
import math

# COMO EU FIZ
num = int(input('Digite um número:'))
numx2 = num * 2
numx3 = num * 3
numxx2 = math.sqrt(num)

print(f'O dobro deste número é: {numx2}'
      f' \nO triplo desse número é: {numx3} \nA raiz quadrada desse número é: {numxx2:.2f}')

# OUTRA FORMA DE SER FEITO
n = int(input('Digite aqui um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)          # forma de exponênciação da raiz quadrada, 1/2 entre parentese pra prioridade
print(f'O dobro de {n} é {d}. \nO triplo de {n} vale {t}.\nA raiz quadrada de {n} vale {r:.2f}')

# OUTRO EXEMPLO
nu = int(input('Digite um número:'))
print(f'O dobro de {nu} é {nu * 2}\n'
      f'O triplo de {nu} é {nu * 3}\n'
      f'A raiz quadrada de {nu} é {nu ** (1/2):.2f}')       # Codigo mais limpo e usando menos memória
