"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado,
peça a digitação novamente, até ter um valor correto"""
sex = ''
while sex != 'M' and sex != 'F':
    sex = str(input('Qual o seu sexo? [M/F]: ')).upper().strip()
    if sex != 'M' and sex != 'F':
        print('\033[31mValor não aceito!\033[m Digite novamente')
print('Valor \033[36marmazenado no sistema!\033[m Muito obrigado.')

# CORREÇÃO
sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')