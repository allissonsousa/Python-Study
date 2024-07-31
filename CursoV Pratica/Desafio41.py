"""A confedereção Nacional de Natação precida de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
- Ate 9 anos: Mirim
- Até 14 anos: Infantil
- Ate 19 anos: Junior
- Ate 20 anos: Senior
- Acima: Master
"""
from datetime import date
ano = int(input('Digite aqui o ano de nascimento do atleta: '))
hoje = date.today().year
idade = hoje - ano
categoria = ''
if idade <= 9:
    categoria = 'Mirim'
elif (idade > 9) and idade <= 14:
    categoria = 'Infantil'
elif (idade > 14) and idade <= 19:
    categoria = 'Junior'
elif (idade < 19) and idade <= 20:
    categoria = 'Sênior'
elif idade > 20:
    categoria = 'Master'
print(f'A categoria desse atleta de acordo com a sua idade é : {categoria}')
