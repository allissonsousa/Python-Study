"""Crie um programa que leia nome, ano de nascimento e carteira de trabaho e cadastre-os(com idade) em um dicionario
se por acaso a CTPS for diferente de ZERO, o dicionário recebera tambem o ano de contratação e o salãrio. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Leve em conta que sao 35 de contribuição
para se aposentar"""
from time import sleep
from datetime import date



dados = {
'nome': str(input('Nome: ')),
'idade': date.today().year - (int(input('Ano de nascimento: '))),
'ctps': int(input('Carteira de trabalho (0 não tem): ')),
'contratação': int(input('Ano de contratação: ')),
'salarios': float(input('Salário: R$')),
'aposentadoria' : }



for v, i in dados.items():
    print(f'    - {v} tem o valor {i}')
    sleep(0.7)