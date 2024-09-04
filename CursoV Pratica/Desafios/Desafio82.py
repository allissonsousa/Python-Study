""" Crie um programa que vai ler vários números e coocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores impares digitados respectivamente.
No final mostre o conteúdo das tres listas geradas"""
completa = []
pares = []
impares = []
cont = 'S'
while cont == 'S':
    n = int(input('Digite um número: '))
    completa.append(n)
    cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'''A lista completa é {completa}
A lista de pares é {pares}
A lista de impares é {impares}''')