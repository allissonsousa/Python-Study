"""Faça um programa q leia um ano qualquer e mostre se ele é bissexto"""

ano = int(input('Verificando se um ano é bissexto ou não! Digite aqui o ano: '))
if ano % 400 == 0:
    print('E ano bissexto')     # Eliminei os divisiveis por 400
elif ano % 100 == 0:
    print('Não é ano bissexto')     # Fiz desconsiderar os outros multiplos de 100
elif ano % 4 == 0:
    print('É ano bissexto')     # Verifica se é divisivel por 4
else:
    print('Não é ano bissexto')     # Caso nao seja divisivel por 4 e não se encaixe em nenhuma outra situação

# CORREÇÃO
from datetime import date
a = int(input('Que ano você quer analisar ?'))
if a == 0:
    a = date.today().year       # Extra! Verificar se o ano atual do computador é bissexto
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano {a} é bissexto!')
else:
    print(f'O ano {a} não é bissexto!')

