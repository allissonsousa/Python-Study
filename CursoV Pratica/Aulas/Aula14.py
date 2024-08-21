# ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO
# WHILE
"""for i in range(1, 10):
    print(i)
print('fim')"""

i = 1
while i < 10:
    print(i)
    i += 1
print('Fim')
# -------------

for i in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIm')
# ------------

# CONDIÇÃO DE PARADA
n = 1
while n != 0:   # O laço só acaba quando a condição é falsa
    n = int(input('Digite um número: '))
print('Fim')
# --------

r = 'S'
while r == 'S':
    nu = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] '))
print('Fim')
# ----------

num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par + impar} números, {par} são pares, e {impar} são impares!!')
print('Acabou! ')