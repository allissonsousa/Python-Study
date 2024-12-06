"""Faça um programa que leia nome e média de um aluno, guardando tambem a situção em um dicionário. No final, mostre o
conteúdo da estrutura na tela"""

situacao = ''
nome = str(input('Nome: '))
media = float(input('Média: '))
if media >= 6:
    situacao = 'Aprovado'
elif media < 6:
    situacao = 'Reprovado'
dados = {'nome' : nome, 'media' : media, 'situação' : situacao}
print('-=-' * 30)
print(f'O nome é igual a {dados['nome']}\n'
      f'A média é igual a {dados['media']}\n'
      f'A Situação é igual a {dados['situação']}')

#---------------------------------------
#Correção

aluno =  dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5<= aluno['média'] <7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=-' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')