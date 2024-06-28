# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis
# sobre ele

# Forma q eu fiz

coisa = input('Digite algo:')
print(type(coisa))
print('É um numero?', coisa.isnumeric(), 'É palavra ou número?', coisa.isalnum(), 'É letra?', coisa.isalpha(),
      'Esta escrito em minusculo?', coisa.islower(),'É imprimivel?', coisa.isprintable(), 'É decimal ?', coisa.isdecimal())

# Forma ideal e corrigida

a = input('Digite algo:')
print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços ?', a.isspace())
print('É um número ?', a.isnumeric())
print('É alfabetico ?', a.isalpha())
print('É alfanumérico ?', a.isalnum())
print('Está em maiúscula ?', a.isupper())
print('Esta capitalizado ?', a.istitle())
