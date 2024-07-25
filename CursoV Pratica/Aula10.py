# ESTRUTURA CONDICIONAL E BLOCOS

tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--fim--')
"""Uso obrigatório dos dois pontos depois do if e do else"""

# CONDIÇÃO SIMPLIFICADA

t = int(input('Quantos anos tem o seu carro ?'))
print('Carro novo' if t <= 3 else 'carro velho')
print('--fim--')
"""Não precisa dos dois pontos"""

# -------------------------

nome = str(input('Qual o seu nome ?'))
if nome == 'Allisson':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tão normal...')
print(f'Bom dia {nome} !')

# --------------------------------

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print(f'A sua média foi {m}')
if m >= 6.0:
    print('Sua média foi boa')
else:
    print('Sua média foi ruim! Estude mais')
