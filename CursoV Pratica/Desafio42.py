""" Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostra que tipo de triangulo sera fomrado:
- Equilatero: todos os lados iguais
- Isoceles: Dois lados iguais
- Escaleno: todos os lados diferentes
"""
print('Vamos construir um triângulo!!')
l1 = float(input('Tamanho do primeiro lado: '))
l2 = float(input('Tamanho do segundo lado: '))
l3 = float(input('Tamanho do terçeiro lado: '))
tri = ''
if l1 == l2 and l2 != l3 or l3 == l1 and l2 != l3 or l2 == l3 and l2 != l1:  # ficou feio credo
    tri = 'Isoceles'
elif l1 != l2 and l2 != l3 and l3 != l1:
    tri = 'Escaleno'
elif l1 == l2 and l2 == l3 and l3 == l1:
    tri = 'Equilatero'

if l1 + l2 > l3 and l1 + l3 > l3 and l2 + l3 > l1:
    print(f'Com essas medidas voce pode construir um triângulo {tri}!!!')
else:
    print('Com essas medidas não é possivel formar um triângulo!!')

