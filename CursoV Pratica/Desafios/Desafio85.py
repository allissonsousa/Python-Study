"""Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha
separado os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente"""
par = []
imp = []
todo = []
for i in range(1, 8):
    number = int(input(f'Digite o {i}° valor:'))
    if number % 2 == 0:
        par.append(number)
    else:
        imp.append(number)
todo.append(par)
todo.append(imp)



print('-=-' * 13)
print(f'Os valores pares digitados foram: {sorted(todo[0])}\n'
      f'Os valores impares digitados foram: {sorted(todo[1])}')

#----------------
# Correção
num = [[],[]]
for c in range(1, 8):
    val = int(input(f'Digite o {0}° valor: '))
    if val % 2 == 0:
        num[0].append(val)
    else:
        num[1].append(val)

print('-=-' * 12)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valres impares digitados foram: {num[1]}')
