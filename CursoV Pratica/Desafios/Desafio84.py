""" Faça um programa que leia no nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
quantas pessoas foram cadastradas
uma listagem com as pessoas mais pesadas
uma listagem com as pessoas mais leves
"""
from platform import win32_edition

person = list()
group = list()
plus = heavy = light = 0
fat = ''
skin = ''
while True:
    name = str(input('Nome: '))
    weight = int(input('Peso: '))
    plus += 1
    person.append(name)
    person.append(weight)
    group.append(person[:])
    want = str(input('Quer continuar? [S/N]'))
    if plus == 1:
        light = weight
    if weight >= heavy:
        heavy = weight
        fat = name
    if weight <= light:
        light = weight
        skin = name

    person.clear()
    if want in 'Nn':
        break

print('-=-' * 13)
print(f'Ao todo, foram cadastradas {plus} pessoas! \n'
      f'O maior peso foi de {heavy}. Peso de {fat} \n'
      f'O menor peso foi de {light}. Peso de  {skin}')

#--------------------------------
#Correção
temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('QUER CONTINUAR? [S/N]'))
    if resp in 'Nn':
        break


print('-=-' * 12)
print(f'Ao todo, voce cadastrou {len(princ)} pessoas\n'
      f'O maior peso foi de {mai}. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print( p[0],end=' ')

print(f'\nO menor peso foi de {men}. Peso de ',end=' ')
for p in princ:
    if p[1] == men:
        print( p[0],end='')
