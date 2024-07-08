from math import sqrt, ceil  # importação de apenas dois modulos
num = int(input('Digite um número:'))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {ceil(raiz)}')  # Ceil é o arredontamento para cima, floor é pra baixo
