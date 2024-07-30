"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se ja passou do tempo do alistamento
Seu programa tambem deve mostrar o tempo que falta ou passou do prazo
"""
from datetime import date
print('Receba aqui informações sobre o seu alistamento militar.')
ano = int(input('Digite aqui o seu ano de nascimento: '))
data = date.today()  # pega a data atual
hoje = data.year  # pega so o ano da data atual
idade = hoje - ano
if idade < 18:
    print('Você é muito jovem, ainda não é hora de se alistar.')
elif idade == 18:
    print('Você ja tem 18 anos, está na hora de fazer o seu alistamento!')
elif idade > 18:
    print(f'Ja passou do tempo de fazer o seu alistamento, você está {idade - 18} anos atrasado! ')
