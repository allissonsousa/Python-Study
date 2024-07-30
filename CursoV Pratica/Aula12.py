# CONDIÇÕES ANINHADAS

# Condições simples: fazem uso só do IF
# Condições compostas: fazem uso do IF e do ELSE
# Condições aninhadas: fazem uso do IF, ELSE e do ELIF

nome = str(input('Qual é o seu nome ?'))
if nome == 'Alinho':
    print('Que belo nome voce tem meu camarada!')
elif nome == 'Pedro' or nome == 'Lucas' or nome == 'Paulo' or nome == 'Marcos':
    print('Você tem um nome bem comum ')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino senhorita')
else:
    print('Seu nome é bem fulera')
print(f'Passar bem {nome}')