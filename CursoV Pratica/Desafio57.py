"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado,
peça a digitação novamente, até ter um valor correto"""
sex = ''
while sex != 'M' and sex != 'F':
    sex = str(input('Qual o seu sexo [M/F]: ')).upper()
    if sex != 'M' and sex != 'F':
        print('\033[31mValor não aceito!\033[m Digite novamente')
print('Valor \033[36marmazenado no sistema!\033[m Muito obrigado.')
