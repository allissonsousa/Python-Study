"""Crie um programa que leia o nome de  uma pessoa e diga se ela tem Silva no nome """
nome = str(input('Digite aqui o seu nome:'))
silva = str('SILVA' in nome.upper())
print(silva.replace('True', 'Você pertençe a família silva 😊').replace('False', 'Voce não pertençe a família silva 😢'))

""" O verificador IN passa um valor em boleano confirmando se tem silva ou nao no nome, este valor é transformado em 
string, e essas strings sao transformadas com o replace"""

# OUTRA FORMA DE SER FEITO
name = str(input('QUal é o seu nome completo?')).strip()
print('Seu nome tem silva ? {}'.format('silva' in name.lower()))