"""Crie um programa onde o usuário digite uma expressão qualquer que use parenteses. Seu aplicativo deverá analisar
se a expressão passada esta com parenteses abertos e fechados na ordem correta"""
exp = str(input('Digite uma expressão: ')).strip()
ls = []
for i in exp:
    ls.append(i)

if ls.index('(') < ls.index(')') and ls.count('(') == ls.count(')') and ls[len(ls) - 1] != '(':
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')


