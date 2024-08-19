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