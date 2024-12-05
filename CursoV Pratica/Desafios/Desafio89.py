"""Crie um programa que leia nome e duas notas e guarde tudo em uma lista composta. No final, mostre um boletim
contendoa  média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente"""

aluno = []
geral = []
cont = 0
while True:
    nome = str(input('Nome: '))
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    aluno = [nome, n1, n2]
    geral.append(aluno[:])
    aluno.clear()
    cont += 1
    if continua == 'N':
        break

print('=-=' * 16)
print(f'No°  NOME          MÉDIA')
print('--' * 15)
for i in range(0, len(geral)):
    media = (geral[i][1] + geral[i][2]) / 2
    print(f'{i}   {geral[i][0]}                 ',end = f'{media}\n')
print('--' * 20)

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe):  '))
    if mostrar == 999:
        break

    print(f'As notas de {geral[mostrar][0]} são: [{geral[mostrar][1]}, {geral[mostrar][2]}]')

    print('--' * 20)


#------------------------
#CORREÇÃO

ficha = list()
while True:
    name = str(input('Nome: '))
    note1 = float(input('Nota 1: '))
    note2 = float(input('Nota 2: '))
    med = (note1 + note2) / 2
    ficha.append([name, [note1, note2], med])
    answ = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if answ == 'N':
        break

print('-=-' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('Finalizado')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<<VOLTE SEMPRE>>>>')