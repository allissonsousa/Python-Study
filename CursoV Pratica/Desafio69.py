"""Crie um programa que leia a idade e o sexo de varias pessoas. Cada pessoas cadastrada, o programa deverá consultar
se o usuário quer ou não continuar. No final mostre
A =  quantas pessoas tem mais de 18 anos
B = quantos homens foram cadastrados
C =  quantas mulheres tem menos de 20 anos"""
continua = 'S'
maiores = 0
homens = 0
mulheres = 0
while continua == 'S':
    print('Cadastre uma pesoa'.center(40, '-'))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    continua = str(input('Voce deseja continuar? [S/N]')).strip().upper()
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 18:
        mulheres += 1

print('Programa encerrado'.center(40, '-'))
print(f'''{maiores} Pessoas que foram cadastradas tem mais de 18 anos!
{homens} Homens foram cadastrados!
{mulheres} Das mulheres cadastradas tem menos de 18 anos!''')

# CORREÇÃO
tot18 = totH = totM = 0
while True:
    age = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F]')).strip().upper()[0]
    if age >= 18:
        tot18 += 1
    if sex == 'M':
        totH += 1
    if sex == 'F' and age < 20:
        totH += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM} mulheres com menos de 20 anos')
