"""Desenvolva um programa que leia o nome, idade, sexo de 4 pessoas, no final do programa mostre:
A media de idade do grupo
Qual o nome do homem mais velhos
Quantas mulheres tem menos de 20 anos"""
velho = 0
maisve = ''
menos = 0
media = 0
for i in range(1, 5):
    nome = str(input(f'Nome da {i} pessoa: '))
    sex = str(input(f'Sexo da {i} pessoa: ')).upper()
    ida = int(input(f'Idade da {i} pessoa: '))
    media += ida / 4
    if sex == 'M' and i == 1:
        velho = ida
    else:
        if ida > velho:
            velho = ida
            maisve = str(nome)
    if ida < 20 and sex == 'F':
        menos += 1
print(f'''
A média de idade desse grupo de pessoas é {int(media)} anos!
O homem mais velho desse grupo é o {maisve}!
{menos} Mulheres desse grupo tem menos de vinte anos!''')

# CORREÇÃO
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for i in range(1, 5):
    print(f'----------------- {i}° PESSOA -------------------------')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20:
        totmulher20 += 1
    mediadidade = somaidade / 4
print(f'A média de idade do grupo é de {mediadidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
